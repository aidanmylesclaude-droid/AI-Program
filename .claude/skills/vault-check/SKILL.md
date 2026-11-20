---
name: vault-check
description: Weekly read-only health check of the AI-Program vault (inbox, unresolved links, orphans, outdated notes, secrets scan). Reports and proposes; changes nothing without the user's OK.
disable-model-invocation: true
---

# Vault check (weekly, from 99-System/MAINTENANCE.md)

Work in the AI-Program folder. **Read-only:** do not create, edit, move or delete anything during the check.
Skip these folders entirely: `.git`, `.obsidian`, `.venv`, `.claude`, `Obsidian`, and anything under `01-University/exercises/`.
Never open `.env` files (they are blocked anyway).

## Checks
1. **Inbox:** list each item in `00-Inbox/` that isn't marked "parked". For each, suggest where it should go (concept note, project idea, tool review, parked, delete).
2. **Unresolved links:** find `[[links]]` in `.md` files whose target note doesn't exist. Ignore links inside backticks or code blocks, and template placeholders like `[[...]]`. Treat `[[name|alias]]` and `[[folder/name]]` as pointing to `name.md`.
3. **Orphans:** notes in `02-Knowledge/concepts/` that no other note links to.
4. **Outdated:** notes with `status: outdated` that don't say what replaced them.
5. **Secrets scan:** search for things that look like real keys or passwords (`sk-`, `api_key=`, `password=`, `token=` followed by a value). Report file and line only, **never print the value**. Known fake example values in lessons are fine: say so.

## Report format
A short table per check (or "none found"), then **Proposed actions** as a numbered list, each one small and specific.
End with: "Nothing was changed. Tell me which proposed actions to do."
Cite file paths for every finding.
