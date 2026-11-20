# My current stack

Only things that are **actually installed and configured** go here. Ideas belong in `tool-reviews/`.

**How this page stays true (stack advisor, Lesson 3.C):**
- New tool seen in a video or link → type `/tool-review <name or link>` in AI-Program. It writes a review in `tool-reviews/` and never installs anything. Only "implement now" + your OK puts a tool in the table below.
- Monthly (`99-System/MAINTENANCE.md`): confirm every row is still true (installed, version, cost); send "later" items whose stage has arrived to `/tool-review`.
- Every "no" goes in **Deliberately NOT installed**, with the reason, so the same tool isn't re-debated.

| Tool | What it does for me | Status | Monthly cost | Added | Review note |
|---|---|---|---|---|---|
| Claude Code | AI agent in the terminal | installed | (part of the Claude plan) | before 2026-11-16 | n/a |
| Python 3.15.2 | Runs scripts (use `py`, not `python`) | installed | free | before 2026-11-16 | n/a |
| Git for Windows 2.56.1 | Version control: snapshots and undo | installed (official installer, `C:\Program Files\Git`; Git added to PATH). Verified by Claude running `git.exe --version` | free | 2026-11-18 | Lesson 1.3.1 |
| pytest 9.2.0 | Automated tests (foundation for Stage 4 evals) | installed **per project venv** (first: `sandbox-3.4\.venv`), never globally | free | 2026-11-20 | Lesson 3.4 |
| Obsidian | Vault viewer and editor | **installed 2026-11-20** (`%LOCALAPPDATA%\Programs\Obsidian`); vault = `AI-Program`; restricted mode, no community plugins | free (Sync $4–5/mo and Publish $8–10/mo not needed: Git backs up) | | |

## Claude Code security settings (user level, `~\.claude\settings.json`)
| Setting | Why | Added |
|---|---|---|
| `deny: Read(//**/.env)`, `Read(//**/.env.*)` | No session in any project can read or edit `.env` files (tested: Read tool and `Get-Content` both blocked) | 2026-11-20, Lesson 3.1 |
| `disableBypassPermissionsMode: "disable"` | Bypass mode is never used on this PC | 2026-11-20, Lesson 3.1 |

## Connectors in Claude Code sessions (checked 2026-11-20, Lesson 3.3)
| Connector | Tools | Status |
|---|---|---|
| Claude Docs | 8 | on |
| scheduled-tasks (built in) | 6 | on (unused until Stage 5) |
| Gmail | 31 | **off** for Code sessions (default off for new ones); still connected on claude.ai. Switch on per task via + → Connectors |

## Skills I made
| Skill | Where | Use | Added |
|---|---|---|---|
| `vault-check` | `AI-Program/.claude/skills/vault-check/` (project) | Type `/vault-check` weekly; read-only report + proposals | 2026-11-20, Lesson 3.2 |
| `tool-review` | `AI-Program/.claude/skills/tool-review/` (project) | Type `/tool-review <tool>`; writes one review in `tool-reviews/`, never installs | 2026-11-20, Lesson 3.C |

## Deliberately NOT installed (and why)
- **LangChain:** established, but overlaps Claude Code + Anthropic SDKs and hides the agent loop you need to learn; untested on Python 3.15. Review: `tool-reviews/langchain.md` (2026-11-20). Re-review only for a concrete multi-provider need.
- **Hooks (none yet):** deny rules already enforce the `.env` rule; every hook runs real commands, so add one only for a specific need (likely logging, Stage 5). 2026-11-20, Lesson 3.2.
_Fill this in as the Optimization Center reviews things. This list is how we stop tool-chasing._
- **Obsidian MCP server / community plugins:** Claude Code reads the vault directly; a bridge adds third-party code, a key and attack surface (Lesson 2.2, 2026-11-20). Revisit only if a chat app needs the vault.
