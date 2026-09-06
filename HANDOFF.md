# HANDOFF — resume point for this clone of ai-software-factory

**Read this first each new session, then [`docs/index.md`](docs/index.md).**
This file is the live "what to do next". `docs/` is the standing reference and
should not be duplicated here — open it instead.

There is no `CLAUDE.md` at this repo root. The only standing conventions are the
global `~/.claude/CLAUDE.md`.

---

## What this repo is

A private clone of [coleam00/ai-software-factory](https://github.com/coleam00/ai-software-factory),
kept so Simon can follow Cole's development week to week and eventually build his own
factory. **No factory runs here.** This repo is the installer (`bin/`) plus the template
(`template/`) that `factory init` copies into a *target* repo.

## Current state (as of 988a929, pushed; this handoff refresh is the next commit)

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

- **Repo made independent of Cole's.** `origin` is now
  `az9713/ai-software-factory` (**private**). Cole's repo is `upstream`, and its push URL
  is set to `DISABLED_never_push_to_cole`, so `git push upstream` fails loudly. Simon's
  commits cannot travel upstream.

- **Two git aliases added** (local to this clone, in `.git/config`):
  `git whatsnew` (fetch + list Cole's new commits, changes nothing) and
  `git sync` (fetch + merge + push to origin). Both tested.

- Working tree clean apart from `.ignore/` — Simon's own terminal captures, untracked
  deliberately, not written by Claude. Local matches `origin/main` (verified via
  `git ls-remote`). Ahead of `upstream/main` (`51778f6`) by docs commits only.

## Next task

**Nothing is in flight.** Simon has not chosen his next move. Three candidates, in the
order the 2026-09-05 review ranked them:

0. **Act on the review** — the anchor grep, the three build exercises, or the Archon
   retry (all listed under Current state). Each is a section, not a new file.

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

None. The 2026-09-05 review was reading, `grep`, and two offline commands
(`_selftest.py`, `watchdog.py --explain`) — no scripts written, nothing to regenerate.

## Known constraints

- **Cole's repo has no LICENSE and the README never mentions licensing**, so his code is
  default copyright. That is why `az9713/ai-software-factory` is **private**. Revisit
  only if he adds a licence.
- **Never push to `upstream`.** Enforced by the broken push URL, not by memory.
- **Do not run `factory init` in this folder.** It would turn a clean reading copy into a
  running factory and guarantee merge conflicts with Cole forever.
