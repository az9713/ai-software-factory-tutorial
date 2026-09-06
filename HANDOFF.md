# HANDOFF — resume point for ai-software-factory-tutorial

**Read this first each new session, then [`docs/index.md`](docs/index.md).**
This file is the live "what to do next". `docs/` is the standing reference and
should not be duplicated here — open it instead.

There is no `CLAUDE.md` at this repo root. The only standing conventions are the
global `~/.claude/CLAUDE.md`.

---

## What this repo is

A tutorial clone of [coleam00/ai-software-factory](https://github.com/coleam00/ai-software-factory),
kept so Simon can follow Cole's development week to week and eventually build his own
factory. **No factory runs here.** This repo is the installer (`bin/`) plus the template
(`template/`) that `factory init` copies into a *target* repo.

Renamed to `az9713/ai-software-factory-tutorial` and made public on 2026-09-05 —
see "Current state" below for the full record.

## Current state (as of `e1b1447`, pushed; this handoff refresh is the next commit)

- **2026-09-05: GitHub Pages enabled, `docs/` is now a live site.** Source is
  main branch, `/docs` folder (`gh api repos/az9713/ai-software-factory-tutorial/pages`,
  build type `legacy`) — `docs/index.html` serves as the site root at
  **https://az9713.github.io/ai-software-factory-tutorial/** (verified HTTP 200,
  first build `built` in ~38s). Linked from the README banner (`e1b1447`). Known
  gap, not fixed: `docs/index.html` links out to `../README.md` and three
  `../template/*.md` files — those 404 on the live site since Pages only serves
  `docs/`; they still work when browsing the repo itself on GitHub. Fix only if
  Simon asks — likely answer is rewriting them to `github.com/.../blob/main/...`
  URLs.

- **2026-09-05: renamed to `az9713/ai-software-factory-tutorial` and made public**,
  against the "Known constraints" note below about Cole's repo having no LICENSE.
  Simon confirmed proceeding anyway when asked directly, framed explicitly as a
  tutorial clone (README banner, `HANDOFF.md` intro above). `origin` remote URL
  updated locally to match; `upstream` (Cole's repo) untouched and still named
  `ai-software-factory`. Do not re-ask — this was a deliberate, confirmed call,
  not an oversight to flag again.

- **2026-09-05 (earlier, `3c428d4`): 22 diagrams added to Simon's five docs, plus new
  sections on what the docs had not covered.** Diagrams are ```` ```mermaid ```` fences in the
  `.md` (GitHub renders them natively). `scripts/md_to_html.py` now pre-renders each
  fence to inline SVG with **mermaid-cli** (`mmdc`, already installed globally via
  npm) driven through the **system Chrome** at
  `C:\Program Files\Google\Chrome\Application\chrome.exe` (override with the
  `DOCS_CHROME` env var). No CDN, so the HTML reads offline. The script fails loudly
  if `mmdc` or Chrome is missing; it does not fall back. Full rebuild takes about two
  minutes (one Chrome launch per diagram). Mermaid gotchas hit and worked around:
  labels beginning `1.` render as "Unsupported markdown: list"; `--flag` text in an
  edge label must be quoted; `#12` in a label is eaten; an edge drawn to a whole
  subgraph overrides that subgraph's `direction`. Colour code in every diagram:
  teal border = code/script, orange = model node, red = human or terminal.

  | Doc | Diagrams | New text |
  |---|---|---|
  | `index.md` | 1: the two-repo picture with GitHub as the bus | — |
  | `key-concepts.md` | 6: the dial's path, issue + PR state machines from `TRANSITIONS`, lock lifecycle, notification chain, ROOT vs SHARED | where the dial lives (`bin/factory.py:589`), the shared `rejected` row, the five `notify.send` sites, env vars under `factory arm`, model tiers in `config.py` are decorative |
  | `one-lap.md` | 11: the lap, the tick's six phases, five node graphs, what the judge sees, the gate decision, the merge, a sequence diagram | "Who talks to whom" section, the stale-read hazard (`escalated_here`) |
  | `component-map.md` | 3: the layers, data between nodes, process topology | "How data moves between nodes" table, "Who is a process" |
  | `study-guide.md` | 1: the holdout / mutation / ratchet triad | — |

  Cole's `first-hour.md` and `incidents.md` are untouched (they exist in `upstream`;
  editing them invites merge conflicts). Their HTML was regenerated unchanged.

  **One real defect found while drawing, deliberately not reported to Cole:** on Windows,
  `template/.factory/notify.sh:89` reports `NOTIFIED via desktop` without showing a
  toast (the PowerShell line only loads a type; no `Show()`). Verified by running a
  copy of the script here. Documented in `docs/key-concepts.md` under the
  notification chain. Simon decided on 2026-09-05 not to file it upstream.

- **2026-09-05: HTML versions of every `docs/*.md` file, `.md` sources untouched.**
  Built with `scripts/md_to_html.py` (new file, kept — it is the reproducible source
  of the HTML, not a one-off scratch script). Uses Python's already-installed
  `markdown` package (`fenced_code`, `tables`, `toc`, `sane_lists` extensions) — no
  new dependency added, this is not a Node project. Dark-mode template inline in the
  script, matching the house HTML style from global `CLAUDE.md`.

  - Converts all seven: `index.html`, `key-concepts.html`, `one-lap.html`,
    `component-map.html`, `study-guide.html`, `first-hour.html`, `incidents.html`.
  - Rewrites same-directory `*.md` links (including `#anchor` fragments) found in the
    converted HTML to point at the sibling `.html` file instead of the `.md` source —
    e.g. `docs/index.html` now links `key-concepts.html`, not `key-concepts.md`.
    Links outside `docs/` (`../README.md`, `../template/...`) are left alone since
    those files are not converted.
  - `docs/git-setup.html` already existed from a prior session (no `.md` source,
    published separately as an Artifact) — untouched, not regenerated by this script.
  - Re-run any time with `python scripts/md_to_html.py` from the repo root; it
    overwrites all seven `.html` files in place and is safe to re-run repeatedly.
    Since the diagram work it also needs `mmdc` and Chrome (see the entry above).

- **2026-09-05: a read-only review of the docs against the original objective.** No repo
  changes. The objective is at `.ignore/cc1_cole.txt:64` with Simon's three answers at
  lines 187–193: (1) follow Cole week to week, (2) build his own version, (3) principles /
  architecture / components, (4) the Archon YAML node schema. Verdict, delivered in chat:

  | Part | Score |
  |---|---|
  | 3. principles / components | exceeded — leave it alone |
  | 4. Archon YAML | met, limited to fields this pack uses (`archon.diy/docs` gave an SSL error) |
  | 1. follow Cole | met on paper, **never fired** — `upstream/main` is still `51778f6` |
  | 2. build his own | partly met — both paths specified, no exercise that changes a file |

  Verified today: every `file.py:NN` anchor in `docs/` resolves; `_selftest.py` prints
  `SELFTEST_PASSED checks=229`; `watchdog.py --explain` matches the table;
  `SLACK_CAPS_AUTONOMY` defaults `false` at `config.py:243`.

  Suggested next levels (not done, Simon has not chosen): a grep in `index.md` that lists
  the line anchors so a Cole commit can be checked against them; three build exercises in
  `study-guide.md` Session 3 (an eighth watchdog detector, stub `dispatch.py:281`, a
  `PreToolUse` deny hook on `.factory/holdout/**`); retry `archon.diy/docs` once.

- **`.ignore/` layout, for the record.** `cc1`, `cc2`, `cc3_cole.txt` are one session
  (the docs build) captured three times at growing length; `cc5_cole.txt` is the second
  session (Archon questions, eight roles, prompt audit). There is no `cc4`.

- **Onboarding docs written and pushed** — five files in `docs/`, 1,500 lines. They fill
  the code-level gap Cole's own docs leave (his cover installing and operating; none read
  the runtime).

  | File | Job |
  |---|---|
  | `docs/index.md` | navigation; the two-repo model |
  | `docs/key-concepts.md` | ~40 terms, each with the file that enforces it |
  | `docs/one-lap.md` | one issue traced filed → merged through the real code |
  | `docs/component-map.md` | every file; code vs prompt; Archon-coupled vs portable |
  | `docs/study-guide.md` | reading order, offline exercises, following upstream |

  Landed in `0e7aaf2`; corrected for the new remote layout in `5419a2a` and `30938cf`.

- **`docs/component-map.md` got an "The eight roles" subsection** (`94c59b7`), just
  before "Workflow-level fields" in the Archon section — a plain, numbered list naming
  the eight jobs Archon does for this repo, each tied to a row in the existing
  portability table further down. No other doc changed.

- **A `/claude-api prompt-audit` ran over the whole `template/` prompt surface**
  (skills, workflow YAML, command files, `MISSION.md`/`FACTORY.md`/`FACTORY_RULES.md`,
  the holdout/e2e docs — 20 files, ~2,100 lines). Read-only, no repo changes.
  **Result: clean.** No dated prompting patterns (pressure language, step-by-step
  scaffolds, prefill/JSON forcing, stale model pins) survived review at high or medium
  confidence. One low-confidence flag only — four "no longer" phrasings
  (`FACTORY_RULES.md:141`, `judge.md:76`, `factory-holdout/SKILL.md:59`,
  `factory-setup/SKILL.md:27`) — judged load-bearing context, not fossils, and left
  alone. This does not need re-running unless the template's prompt files change.

- **`docs/git-setup.html`** (`1202f2c`) — the git setup explained for someone new to git:
  what a remote is, the two-remote diagram, the three locks, why a fork/plain clone/no
  remote/extra branch were each rejected, the sync routine, and `git merge --abort` as the
  escape hatch. Dark house style per global CLAUDE.md. Also published privately at
  https://claude.ai/code/artifact/fcf61e7c-881b-447a-b8b5-211d3bf3a556
  (this session's watch on it has ended; re-watch only if needed).

- **Repo made independent of Cole's.** Cole's repo is `upstream`, and its push URL
  is set to `DISABLED_never_push_to_cole`, so `git push upstream` fails loudly. Simon's
  commits cannot travel upstream.

- **Two git aliases added** (local to this clone, in `.git/config`):
  `git whatsnew` (fetch + list Cole's new commits, changes nothing) and
  `git sync` (fetch + merge + push to origin). Both tested.

- Working tree clean. `.ignore/` (Simon's own terminal captures) is now in
  `.gitignore` (`0259b95`) so it no longer shows as untracked noise. Local matches
  `origin/main` (verified via `git ls-remote` after each push, latest `e1b1447`).
  Ahead of `upstream/main` (`51778f6`) by docs commits only; Cole's files are
  untouched, so `git sync` stays conflict-free.

## Next task

**Nothing is in flight.** Simon has not chosen his next move. Candidates, newest first:

0. ~~Decide on the Windows toast defect~~ **Decided 2026-09-05: do NOT file it
   upstream.** Simon said "no filing". Nothing was ever created on Cole's repo
   (verified: no issue or PR by az9713 there). The finding stays documented locally in
   `docs/key-concepts.md`. Do not re-ask.
0. **Act on the earlier review** — the anchor grep, the three build exercises, or the
   Archon retry (all listed under Current state). Each is a section, not a new file.
0. **Two diagram choices Simon may overturn:** mermaid layout with the house palette
   (vs hand-drawn SVG), and only one diagram in `study-guide.md`. Rebuild with
   `python scripts/md_to_html.py` after any `.md` edit; needs `mmdc` + Chrome.

The two standing paths, from `docs/study-guide.md`:

1. **Read and run** — Session 2 (the code, ~3 hours) and Session 3 (four offline
   commands, all verified working). Then install into a throwaway repo and work
   `docs/first-hour.md` in order.
2. **Build his own factory** — `factory init` in a *different* folder, never this one.
   Path A (adapt the template, keep Archon) vs Path B (rebuild on Claude Code, no
   Archon) are both specified in `docs/study-guide.md`. Simon said "both — understand
   it, then decide", so the decision is still open.

If Simon asks for something else, that takes precedence.

## Where to read things (reference, don't re-derive)

| Path | What |
|---|---|
| https://az9713.github.io/ai-software-factory-tutorial/ | the live site — `docs/` rendered as GitHub Pages |
| `docs/index.md` | the map, and the two-repo model |
| `docs/one-lap.md` | the full trace — read this before changing anything |
| `docs/component-map.md` | what is Archon-coupled (7 shell-outs) vs portable (~5,000 lines) |
| `README.md` | Cole's pitch, the autonomy dial, the command list |
| `docs/first-hour.md` | Cole's post-install checklist |
| `docs/incidents.md` | Cole's failure log — the architecture-decision record, 1,326 lines |
| `template/FACTORY_RULES.md` | the rulebook every workflow reads at run start |

## Following Cole

```bash
git whatsnew                                          # what he has that you do not
git log -p main..upstream/main -- docs/incidents.md   # read the new incidents in full
git sync                                              # take it, and push to your repo
```

Cole publishes **no releases and no tags** — one branch, `main`. His newest commits on
`main` are the only thing to track. He moved fast: 74 commits between 2026-08-31 and
2026-09-02.

**Merges stay clean as long as edits go in files Cole does not have.** All five doc files
are new names. If a conflict ever appears, `git merge --abort` undoes it losing nothing.

## Session-transient scratch

None that matters. The diagram session rendered PNG previews of individual diagrams in
the scratchpad to check them by eye (the Chrome extension refuses `file://` URLs); the
pattern is `mmdc -i x.mmd -o x.png -s 1.5 -p pp.json -c theme.json`, with `pp.json` and
`theme.json` dumped from `md_to_html.py`'s `CHROME` and `MERMAID_THEME`. The durable
record is the committed `docs/*.html`; the generator is the committed script. The
mermaid syntax traps are in memory (`mermaid-cli-offline-svg`), not here.

## Known constraints

- **Cole's repo has no LICENSE and the README never mentions licensing**, so his code is
  default copyright. `az9713/ai-software-factory-tutorial` was kept **private** for that
  reason, then made **public** on 2026-09-05 as a deliberate, explicitly-labelled
  tutorial clone (Simon's call, README banner names it as such). Still no licence on
  Cole's repo as of that date — this is a known, accepted risk, not an oversight.
- **Never push to `upstream`.** Enforced by the broken push URL, not by memory.
- **Do not run `factory init` in this folder.** It would turn a clean reading copy into a
  running factory and guarantee merge conflicts with Cole forever.
