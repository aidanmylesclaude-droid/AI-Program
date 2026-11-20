# Conventions

- **Numbered top folders** (`00-`, `01-`...) keep the order the same everywhere: in Explorer, in the terminal and in Obsidian.
- **File names:** lowercase-with-dashes. Lessons start with their ID (`1.1.1-...`). Session logs use `YYYY-MM-DD.md`. Tool reviews use the tool name (`obsidian-mcp.md`).
- **One idea per concept note.** If you're writing "and also...", start a second note and link the two.
- **Links:** `[[note-name]]` (Obsidian style). Claude follows them as file paths.
- **Dates:** always absolute (2026-11-16), never "last week".
- **Status words:** `draft`, `active`, `outdated`. Outdated notes say what replaced them and get moved to an archive in Stage 2.
- **No secrets** in any note, ever.
- **Templates:** `99-System/templates/`.
- **Note types and where they live (Lesson 2.3):**
  | Type | What | Where |
  |---|---|---|
  | Temporary | Raw ideas, links, tangents | `00-Inbox/` (sort it weekly) |
  | Active | What we're working on now | `01-University/` (PROGRESS, current lesson) |
  | Permanent | One idea, in your own words, linked | `02-Knowledge/concepts/` |
  | Reference | Facts to look up: decisions, project briefs, tool reviews, stack | `02-Knowledge/decisions/`, `projects/`, `03-Optimization-Center/` |
  | Long-term record | What happened, kept as history | `02-Knowledge/sessions/`; outdated notes go to an archive |
- **Folder, link or tag?** Folder = where a note lives (one place). Link = a specific connection between two notes. Tag = a broad theme across folders (`#security`, `#trading`). Prefer links; keep tags few.
- **Properties:** new concept notes start with a `---` block (`type`, `status`, `tags`, `created`, `lesson`). Never put secrets in properties either.
