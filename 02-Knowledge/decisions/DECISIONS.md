# Decision log

Newest entries go first. Each entry: date, decision, why, and what would make us revisit it.

## 2026-11-19: Fast mode. Claude runs the exercises; the user predicts and answers
- **What:** the user asked Claude to "take control and finish everything". Claude can't do the learning for them, so the compromise is: Claude runs commands and shows output, and the user predicts first and answers 2-question checks. The user still does installs, accounts, sign-ins and approvals.
- **Why:** most time was going to typing, pasting and joined-command errors, not learning. Predictions keep the learning active.
- **Revisit if:** knowledge-check results drop, or before Stage 4 (building agents), where hands-on practice matters more.

## 2026-11-19: Curriculum condensed (remaining ~51 lessons → 34)
- **What:** merged overlapping lessons. Module 1.5's 1.5.3–1.5.11 became 1.5.3–1.5.6; Module 1.6 went from 8 lessons to 4; Stage 2 from 7 to 4; Stage 3 from 9 to 5 (hands-on setup only, no re-teaching). Stages 4–6 unchanged. Lessons are also leaner: one-line commands and 2-question checks.
- **Why:** the user asked to go faster. Real overlap existed (Stage 3 re-reviewed Module 1.5 topics; 1.6 repeated 1.2.3–1.2.4; memory was mostly covered in 1.1.7 and 1.2.4).
- **Kept in full:** 1.5.2 (API keys), agent security (now in 1.6.4), all capstones, Stages 4–6.
- **Revisit if:** a merged lesson feels rushed or knowledge checks start slipping. Then split it back.

## 2026-11-19: Claude commits and pushes AI-Program at the end of every session
- **What:** step 4 of the end-of-session protocol in CLAUDE.md: check for secrets, then commit ("Session YYYY-MM-DD: …") and push to the private `AI-Program` repo.
- **Why:** the GitHub backup only covers what's committed and pushed, and remembering to do it by hand is easy to forget. One commit per session also gives a readable history.
- **Revisit if:** the user wants to review each commit before it's made, or wants more frequent commits during long sessions.

## 2026-11-18: Git from the official installer; GitHub repos are private, and commits use the noreply email
- **What:** Git for Windows installed from git-scm.com, not winget (the site says the winget package isn't maintained by the Git for Windows project). Every GitHub repo is **Private** unless deliberately made public. Global `user.email` is GitHub's noreply address.
- **Why:** official source; trading, content and supplier work is private by nature; a real email in commit history can't be removed later.
- **Revisit if:** a project is meant to be public (then review its history and contents before switching).

## 2026-11-18: Practise on a sandbox before putting AI-Program under Git and GitHub
- **Why:** pushing is hard to undo. `.gitignore` (1.3.4) and a check for anything secret come first.
- **Outcome (2026-11-19):** done. After 1.3.4, AI-Program was put under Git with a `.gitignore` and pushed to a private GitHub repo `AI-Program`.

## 2026-11-17: A short global `~\.claude\CLAUDE.md` holds only what's true in every project
- **Contents:** how the user learns (define terms, why before what, small hands-on steps), the computer (PowerShell 5.1, `;` not `&&`, `py`), and two safety rules (no secrets in notes; secrets in each project's own `.env`; no system folders). Approved by the user in the working session.
- **Why:** Without it, a new project folder (e.g. trading-research) would start with none of these. Everything program-specific stays in `AI-Program\CLAUDE.md`; a small overlap is accepted for now.
- **Revisit if:** the global file grows past ~20 lines, or the overlap with `AI-Program\CLAUDE.md` starts to drift (tidy up in Stage 2).

## 2026-11-16: The program lives in `C:\Users\aidan\AI-Program`, not System32
- **Why:** Claude Code was launched from `C:\WINDOWS\System32`, a core Windows system folder. That folder isn't empty, and writing there risks the OS. The user's home folder is the safe, normal place for personal projects. It's also outside OneDrive, which avoids sync conflicts with Git and Obsidian later.
- **Revisit if:** the user wants it on another drive or synced through a specific backup tool.

## 2026-11-16: One folder = the program = the Obsidian vault
- **Why:** The simplest integration. Claude Code reads Markdown files directly, so no plugin or MCP server is needed. The three areas are sections of one vault instead of three separate systems, so links work across all of them.
- **Revisit if:** the vault grows big enough that search becomes slow or noisy (unlikely for a long time).

## 2026-11-16: Lessons are written when they're taught, not all at once
- **Why:** Tools change fast. Writing lessons just in time keeps them accurate and lets each one adapt to the user's weak spots.
