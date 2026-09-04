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

## Current state (as of 30938cf, pushed)

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

- **Repo made independent of Cole's.** `origin` is now
  `az9713/ai-software-factory` (**private**). Cole's repo is `upstream`, and its push URL
  is set to `DISABLED_never_push_to_cole`, so `git push upstream` fails loudly. Simon's
  commits cannot travel upstream.

- **Two git aliases added** (local to this clone, in `.git/config`):
  `git whatsnew` (fetch + list Cole's new commits, changes nothing) and
  `git sync` (fetch + merge + push to origin). Both tested.

- Working tree clean. Local `30938cf` matches `origin/main`. Three commits ahead of
  `upstream/main` (`51778f6`), all of them docs.

## Next task

**Nothing is in flight.** Simon has not chosen his next move. The two open paths, from
`docs/study-guide.md`:

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

None. Every edit this session went straight into a committed file. The doc corrections
were applied with inline `python - <<PY` heredocs, not saved scripts — nothing to
regenerate.

## Known constraints

- **Cole's repo has no LICENSE and the README never mentions licensing**, so his code is
  default copyright. That is why `az9713/ai-software-factory` is **private**. Revisit
  only if he adds a licence.
- **Never push to `upstream`.** Enforced by the broken push URL, not by memory.
- **Do not run `factory init` in this folder.** It would turn a clean reading copy into a
  running factory and guarantee merge conflicts with Cole forever.
