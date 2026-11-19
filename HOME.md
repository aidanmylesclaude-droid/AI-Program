# Home

This folder is the whole program. It will also become the **Obsidian vault** in Stage 2.
A vault is just a folder of plain-text notes, so Claude Code can already read everything here with no plugins.

## The three areas, and how they feed each other

```
              ┌────────────────────────────┐
              │  00-Inbox (raw captures:   │
              │  videos, links, ideas)     │
              └─────────────┬──────────────┘
                     triage │ (Claude routes each item)
        ┌───────────────────┼───────────────────────┐
        ▼                   ▼                       ▼
 01-University   ◄──►  02-Knowledge  ◄──►  03-Optimization-Center
 (learn: lessons,       (remember: concepts,   (evaluate: tool reviews,
  exercises,             decisions, project      stack, research)
  progress)              briefs, session logs)
        │                   ▲                       │
        └── a lesson ends ──┘   a tool review ──────┘
            with a concept      that's "implement now"
            note                becomes a lesson or an
                                entry in STACK.md
```

- **University → Knowledge.** Each finished lesson produces or updates concept notes. The lesson teaches; the concept note is the short version you and Claude look things up in later.
- **Optimization Center → University.** A tool rated "implement now" gets a hands-on lesson before it gets installed. That rule is what stops tool-chasing.
- **Optimization Center → Knowledge.** Everything installed is recorded in `03-Optimization-Center/STACK.md`. Each choice is logged in `DECISIONS.md`.
- **Knowledge → future agents.** Project briefs in `02-Knowledge/projects/` collect ideas, so nothing is lost while you're still learning.

## Start here
- [[01-University/ROADMAP|Roadmap]]
- [[01-University/CURRICULUM|Curriculum checklist]]
- [[01-University/PROGRESS|Progress, and where we left off]]
- [[00-Inbox/INBOX|Inbox]]
- [[02-Knowledge/decisions/DECISIONS|Decision log]]
- [[03-Optimization-Center/STACK|My current stack]]
- [[99-System/CONVENTIONS|Conventions]]

## How to start a session
1. Open PowerShell.
2. Run `cd $HOME\AI-Program`.
3. Run `claude`.
4. Claude reads `CLAUDE.md` automatically, then checks PROGRESS.md and tells you where you are.
