import pathlib
import re
import markdown

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"

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
    html_body = markdown.markdown(
        text, extensions=["fenced_code", "tables", "toc", "sane_lists"]
    )
    html_body = relink(html_body, stems)
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
