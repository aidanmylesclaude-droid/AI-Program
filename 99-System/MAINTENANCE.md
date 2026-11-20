# Vault maintenance routine
Keeps the second brain findable for you and for Claude. Small and regular beats big and rare.

## Every session (Claude does this at "wrap up", per CLAUDE.md)
- [ ] `01-University/PROGRESS.md`: lesson status and "Where we left off"
- [ ] Session log in `02-Knowledge/sessions/YYYY-MM-DD.md` (3–6 bullets)
- [ ] Real decisions in `02-Knowledge/decisions/DECISIONS.md`
- [ ] Git backup: secret check, commit, push

## Weekly (about 10 minutes; say "vault check" and Claude runs it)
- [ ] **Empty the inbox:** each item in `00-Inbox/` becomes a concept note, a project idea, a tool review, or "parked"/deleted
- [ ] **Unresolved links:** list `[[links]]` with no note yet. Write the important ones (one idea each), drop the rest
- [ ] **Orphans:** notes nothing links to. Link them from somewhere sensible, or ask if they're still needed
- [ ] **Outdated:** anything no longer true gets `status: outdated` and a line saying what replaced it
- [ ] **No secrets:** scan the vault for keys or passwords (`Select-String`)

## Monthly
- [ ] Re-read `HOME.md` and `CONVENTIONS.md`: do they still match how you actually work?
- [ ] Check `03-Optimization-Center/STACK.md` is still true (versions, what's installed)

## Rules
- Rename or move notes **in Obsidian** so links update (Lesson 2.2).
- One idea per concept note, in your own words (Lesson 2.3).
- Possible later upgrade: turn "vault check" into a skill (Stage 3.2).
