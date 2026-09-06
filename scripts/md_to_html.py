import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import markdown

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"

# ```mermaid fences are pre-rendered to inline SVG with mermaid-cli (`mmdc`, needs a
# Chrome), so the HTML is readable offline and GitHub still renders the .md natively.
CHROME = os.environ.get(
    "DOCS_CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe"
)
MERMAID_FENCE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)
MERMAID_THEME = {
    "theme": "base",
    "themeVariables": {
        "darkMode": True, "background": "#0f172a", "fontFamily": "Segoe UI, Helvetica, Arial, sans-serif",
        "fontSize": "14px", "primaryColor": "#1e293b", "primaryTextColor": "#e2e8f0",
        "primaryBorderColor": "#94a3b8", "secondaryColor": "#172033", "tertiaryColor": "#0f172a",
        "lineColor": "#94a3b8", "textColor": "#e2e8f0", "mainBkg": "#1e293b",
        "nodeBorder": "#94a3b8", "clusterBkg": "#172033", "clusterBorder": "#334155",
        "titleColor": "#e2e8f0", "edgeLabelBackground": "#0f172a",
        "actorBkg": "#1e293b", "actorBorder": "#fb923c", "actorTextColor": "#e2e8f0",
        "actorLineColor": "#334155", "signalColor": "#e2e8f0", "signalTextColor": "#e2e8f0",
        "labelBoxBkgColor": "#172033", "labelBoxBorderColor": "#334155", "labelTextColor": "#e2e8f0",
        "loopTextColor": "#e2e8f0", "noteBkgColor": "#172033", "noteTextColor": "#cbd5e1",
        "noteBorderColor": "#334155", "activationBkgColor": "#334155", "activationBorderColor": "#fb923c",
        "sequenceNumberColor": "#0f172a",
    },
    "flowchart": {"curve": "basis", "htmlLabels": False, "padding": 12},
    "sequence": {"mirrorActors": False, "actorMargin": 40, "useMaxWidth": True},
}


def render_mermaid(src: str, svg_id: str) -> str:
    mmdc = shutil.which("mmdc")
    if not mmdc:
        sys.exit("mmdc (mermaid-cli) is not on PATH: npm i -g @mermaid-js/mermaid-cli")
    if not pathlib.Path(CHROME).exists():
        sys.exit(f"Chrome not found at {CHROME}; set DOCS_CHROME to its path")
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        (td / "pp.json").write_text(json.dumps({"executablePath": CHROME, "args": ["--no-sandbox"]}))
        (td / "theme.json").write_text(json.dumps(MERMAID_THEME))
        (td / "in.mmd").write_text(src, encoding="utf-8")
        p = subprocess.run(
            [mmdc, "-i", str(td / "in.mmd"), "-o", str(td / "out.svg"), "-b", "transparent",
             "-I", svg_id, "-p", str(td / "pp.json"), "-c", str(td / "theme.json")],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if p.returncode != 0 or not (td / "out.svg").exists():
            sys.exit(f"mmdc failed on {svg_id}:\n{p.stdout}\n{p.stderr}\n--- source ---\n{src}")
        return (td / "out.svg").read_text(encoding="utf-8")


def extract_mermaid(text: str, stem: str) -> tuple[str, list[str]]:
    # Swap each fence for a placeholder paragraph; put the rendered SVG back after markdown.
    figures: list[str] = []

    def sub(m: re.Match) -> str:
        i = len(figures)
        figures.append(render_mermaid(m.group(1), f"mmd-{stem}-{i}"))
        return f"\nMERMAIDFIG{i}\n"

    return MERMAID_FENCE.sub(sub, text), figures

TEMPLATE = """<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title}</title>
<style>
  :root {{
    --bg: #0f172a; --card: #1e293b; --text: #e2e8f0; --text-dim: #cbd5e1;
    --muted: #94a3b8; --accent: #fb923c; --accent2: #2dd4bf;
    --border: #334155; --code-bg: #1e293b;
  }}
  body {{
    background: var(--bg); color: var(--text);
    font-family: -apple-system, Segoe UI, Helvetica, Arial, sans-serif;
    line-height: 1.6; max-width: 860px; margin: 0 auto; padding: 2.5rem 1.5rem 4rem;
  }}
  h1, h2, h3, h4 {{ color: var(--text); line-height: 1.3; }}
  h1 {{ border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
  h2 {{ border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; margin-top: 2.5rem; }}
  a {{ color: var(--accent2); }}
  p, li {{ color: var(--text-dim); }}
  code {{ background: var(--code-bg); border: 1px solid var(--border); border-radius: 3px; padding: 0.1em 0.35em; font-size: 0.9em; }}
  pre {{ background: var(--code-bg); border: 1px solid var(--border); border-radius: 6px; padding: 1rem; overflow-x: auto; }}
  pre code {{ border: none; padding: 0; background: none; }}
  blockquote {{ border-left: 3px solid var(--accent); margin-left: 0; padding-left: 1rem; color: var(--muted); }}
  table {{ border-collapse: collapse; width: 100%; overflow-x: auto; display: block; }}
  th, td {{ border: 1px solid var(--border); padding: 0.5rem 0.75rem; text-align: left; }}
  th {{ background: var(--card); }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 2rem 0; }}
  figure.diagram {{ margin: 1.5rem 0; padding: 1rem; background: var(--card); border: 1px solid var(--border); border-radius: 6px; overflow-x: auto; }}
  figure.diagram svg {{ display: block; margin: 0 auto; max-width: 100%; height: auto; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""

def title_from(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback

def relink(html_body: str, stems: set) -> str:
    # Point same-directory links at the converted .html file, not the .md source.
    pattern = re.compile(r'href="([a-zA-Z0-9_-]+)\.md(#[^"]*)?"')

    def sub(m: re.Match) -> str:
        stem, anchor = m.group(1), m.group(2) or ""
        if stem in stems:
            return f'href="{stem}.html{anchor}"'
        return m.group(0)

    return pattern.sub(sub, html_body)

def convert(md_path: pathlib.Path, stems: set) -> None:
    text = md_path.read_text(encoding="utf-8")
    text, figures = extract_mermaid(text, md_path.stem)
    html_body = markdown.markdown(
        text, extensions=["fenced_code", "tables", "toc", "sane_lists"]
    )
    html_body = relink(html_body, stems)
    for i, svg in enumerate(figures):
        html_body = html_body.replace(f"<p>MERMAIDFIG{i}</p>", f'<figure class="diagram">{svg}</figure>')
    if figures:
        print(f"  {len(figures)} diagram(s) rendered for {md_path.name}")
    title = title_from(text, md_path.stem)
    html_path = md_path.with_suffix(".html")
    html_path.write_text(TEMPLATE.format(title=title, body=html_body), encoding="utf-8")
    print(f"wrote {html_path}")

def main() -> None:
    md_paths = sorted(DOCS.glob("*.md"))
    stems = {p.stem for p in md_paths}
    for md_path in md_paths:
        convert(md_path, stems)

if __name__ == "__main__":
    main()
