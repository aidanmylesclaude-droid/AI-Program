# Progress

## Where we left off
- **Date:** 2026-11-18 (desktop app, Code tab). Detail is in `02-Knowledge/sessions/2026-11-17.md` and `2026-11-18.md`.
- **Done so far:** **Modules 1.1 and 1.2 complete**; Module 1.3: 1.3.1–1.3.3 done (18 lessons). Global `~\.claude\CLAUDE.md` created. Git installed; GitHub account with a private `git-practice` repo. The user's desktop sessions run in **Auto** mode.
- **Start next session with:** a one-line re-ask of 1.3.3 Q2 ("You push a file with an API key, then delete it in the next commit. Is the key safe?" Answer: no, it's still in history; revoke it).
- **Git:** 2.56.1 at `C:\Program Files\Git`; global `~\.gitconfig` has the user's name and GitHub noreply email. If Claude's shell can't find `git`, use `& "C:\Program Files\Git\cmd\git.exe"`. Trust only Git output pasted straight from a window (earlier unverified output was wrong).
- **1.3.4 done (2026-11-19). Module 1.3 complete.** `sandbox-1.3.1` now has a `.gitignore` (`.env`), pushed as `0924f1b`; `.env` is on disk only. `sandbox-1.3.4` (local only, never pushed) showed the trap: a committed `secrets.txt` stays in history after `rm --cached`.
- **Tip that worked:** give multi-step commands as ONE line joined with `;`. Copying several boxes at once joins them without spaces.
- **Next step:** Ask the user whether to back up `AI-Program` itself as a private GitHub repo (capstone for 1.3): `.gitignore` first (`.env`, `.env.*`, `CLAUDE.local.md`, `.claude/settings.local.json`, and the nested sandbox repos), check for secrets (`sandbox-1.1.5\.env` is fake but should still be ignored), then init, commit, push. Otherwise start Module 1.4 (1.4.1 Reading a Python script line by line).
- **Note:** the user's PowerShell sometimes opens in `C:\WINDOWS\System32`. That is **not always** Administrator: on 2026-11-19 it was a normal window (writes to `C:\Windows` were "Access denied"). Correction to the earlier "System32 = admin" claim. Either way, always start exercises with an **absolute** `cd ~\AI-Program\...` instead of relative `cd ..`.
- **How to teach this user:** predict-then-run checks, low pressure (CLAUDE.md rule; earlier pasted answers came from "not sure I'm right"). Put each command in its own code box and remind them: Enter after each, and only commands go in the terminal.
- **Open items:** Ask what `~\test-project` is (seen in `~\.claude\projects`), at a natural moment. The trading-research project hasn't been shared yet; don't assume anything about it.

## Knowledge-check results
| Lesson | Date | Result | Weak spots to revisit |
|---|---|---|---|
| 1.1.1 | 2026-11-16 | 4/4 (Q2 partial: missed "where files get created") | Q2: the folder also decides where Claude creates and edits files |
| 1.1.2 | 2026-11-16 | 4/4 (Q1 partial: called the shell "the noise"; it's the listener/interpreter) | The shell *interprets*; also `;` isn't an exact match for `&&` |
| 1.1.3 | 2026-11-17 | 2/4 own words, 2 pasted (Q1 partial: right idea, no concrete path; Q3 partial: `ls` without a path; Q2 and Q4 pasted from an outside source) | Re-ask Q2 (`~` = `C:\Users\aidan`) and Q4 (Tab) briefly at the start of 1.1.4; `ls <path>` to peek |
| 1.1.4 | 2026-11-17 | Q1–2 own words ✓ (found `Rename-Item` unprompted); Q3–5 pasted; Set-Content overwrite confirmed by predict-then-run ✓ | `mv` does *not* overwrite in PowerShell; `Set-Content` and `cp` do. Re-check with a predict question |
| 1.1.5 | 2026-11-17 | Predictions in own words: `py hello.txt` runs ✓, broken JSON errors ✓, warm-up copy/`cp` ✗ (said `two`; ran it and saw `one`). Written Q1–4 pasted (correct; added the hidden-extension `settings.json.txt` point) | Copy = independent snapshot vs shortcut/link. Fixed by running it |
| 1.1.6 | 2026-11-17 | 5/5 own words (prediction ✓; gut calls a allow, b ask why, c deny, d deny ✓) | Wrote "sandbox 1.1.5" with a space: names with spaces vs hyphens |
| 1.1.7 | 2026-11-17 | Exercise: JSON ✓, global CLAUDE.md guessed True (was False). Check: 3.5/4 own words (Q4 said "md", not *which* one) | Global `~\.claude\CLAUDE.md` vs project `CLAUDE.md`. Revisit in 1.1.8 |
| 1.1.8 | 2026-11-17 | 3/3 own words (all three CLAUDE.md files load; one `.env` per project; `C--Users-aidan-trading-research`) ✓ | None. Global-vs-project now solid |
| 1.2.1 | 2026-11-17 | Predictions: "market" ✓; "same every time" ✗ (saw sampling). Check: Q1 partial ("using tokens", missed *predict next, repeat*), Q2 ✓ (remembers via files), Q3 ✓ (don't trust a price with no tool) | "Predict the next token, repeat": re-ask once in 1.2.2 |
| 1.2.2 | 2026-11-17 | Re-ask from 1.2.1 ✓. Predictions: chat can't see files ✓; first tool call ✓, count 3 (was 2). Check 4/4 own words ✓ | None |
| 1.2.3 | 2026-11-17 | Predictions 3/3 ✓ (2 steps, step-1 error, 1 step from 01-University). Check 4/4 own words ✓ | Still sometimes types commands into chat, or runs them from the wrong folder. Keep saying where to run each one |
| 1.2.4 | 2026-11-17 | Predictions 2/2 ✓ (rule lost in Part 1, kept when pinned). Check 3/3 own words ✓ | None |
| 1.2.5 | 2026-11-17 | Mode observed: Auto. Prediction "neither prompts" ✓. Check 4/4 own words ✓ | None. Note: in Auto, tool calls are the user's main view of what Claude does, so keep encouraging them to open the tool calls |
| 1.2.6 | 2026-11-17 | Prediction (vague request deletes nothing) ✓. Rewrite had Goal + Where but no Constraints or Done check. Check 3/3 own words ✓ | Writing constraints and done checks into their *own* requests: prompt for them next time they ask for real work |
| 1.2.7 | 2026-11-17 | Catch-Claude exercise 4/4 predicted, then verified on the PC ✓. Check 3/3 own words ✓ | None |
| 1.3.1 | 2026-11-18 | Predictions ✓ (untracked, "Changes to be committed", 1 line, real hash looks random). Check 3/3 own words (Q3 named Git as local, didn't say GitHub is a website) | Earlier unverified output (`a1b2c3d`, a "git version" before Git was installed). Keep asking for pasted window text for anything that matters |
| 1.3.2 | 2026-11-18 | Predictions ✓ (modified; `-` old / `+` new; 3 log lines). Check 3/3 own words ✓ | First pass skipped the damage step. Ask for pasted output before moving on |
| 1.3.3 | 2026-11-18 | Push ✓, GitHub showed 5 commits and Private ✓. Check: Q1 no/yes ✓ (or partial), Q3 privacy ✓. **Q2 possibly answered "yes, the key is safe" ✗** | A pushed secret is never safe, even if deleted later: revoke it. Re-asked 2026-11-19 → answered correctly ✓ |
| 1.3.4 | 2026-11-19 | Predictions ✓ (.env untracked → disappears; password still in history). Check 3/3 own words ✓ (Q1 short: "it's already tracked") | Several "it worked" reports before commands had actually run. Keep verifying from Claude's side |

## Stage status
| Stage | Status |
|---|---|
| 0 Orientation | done |
| 1 Fundamentals | started |
| 2–6 | not started |
