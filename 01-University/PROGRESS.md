# Progress

## Where we left off
- **Date:** 2026-11-19 (desktop app, Code tab). Detail is in `02-Knowledge/sessions/` (2026-11-17, -18, -19).
- **Done so far:** Modules **1.1–1.4 complete**; Module 1.5: **1.5.1–1.5.2 done** (24 lessons). Global `~\.claude\CLAUDE.md`; Git; GitHub (private `git-practice` and `AI-Program` repos). Desktop sessions run in **Auto** mode. **Fast mode** is on (see CLAUDE.md).
- **Current lesson:** **1.5.3** MCP, connectors, integrations and plugins. Written and taught; `claude mcp list` was run (shows claude.ai Gmail + Claude Docs connectors). **Only the 2-question knowledge check is left**: (1) MCP vs MCP server vs connector, (2) why not connect every MCP server from a video. Start next session with it, then 1.5.4 (skills, slash commands, hooks).
- **Open question for Stage 3.1/3.3:** Gmail is connected to every Claude Code session, including this program. Least privilege suggests disabling it here; ask the user.
- **Git:** 2.56.1 at `C:\Program Files\Git`; global `~\.gitconfig` has the user's name and GitHub noreply email. If Claude's shell can't find `git`, use `& "C:\Program Files\Git\cmd\git.exe"`. Trust only Git output pasted straight from a window (earlier unverified output was wrong).
- **1.3.4 done (2026-11-19). Module 1.3 complete.** `sandbox-1.3.1` now has a `.gitignore` (`.env`), pushed as `0924f1b`; `.env` is on disk only. `sandbox-1.3.4` (local only, never pushed) showed the trap: a committed `secrets.txt` stays in history after `rm --cached`.
- **Tip that worked:** give multi-step commands as ONE line joined with `;`. Copying several boxes at once joins them without spaces.
- **AI-Program is backed up (2026-11-19):** a Git repo with `.gitignore` (`.env`, `.env.*`, `CLAUDE.local.md`, `.claude/settings.local.json`, nested sandbox repos 1.3.1 and 1.3.4). First commit `7772fd3` (47 files, no secrets; scan found only fake examples). Pushed to **private** GitHub repo `AI-Program`, verified in sync with `origin/main`.
- **1.4.1 done (2026-11-19):** read `tiny_predictor.py` with the four questions (what it says, reads, changes or sends, where it stops); the safety scan with `Select-String` found nothing; changed the start word to `video`, ran it, then `git diff` + `git restore`.
- **1.4.2 done (2026-11-19):** `sandbox-1.4.2\.venv` holds `requests` 2.34.2 (plus 4 dependencies); the global Python stays clean. `requirements.txt` was made with `pip freeze | Set-Content`. `.venv/` is in AI-Program's `.gitignore`. **Convention:** use a venv **without activating it** (`.venv\Scripts\python.exe ...`), so no execution-policy change is needed.
- **1.4.3 done (2026-11-19). Module 1.4 complete.** Read nested made-up market JSON (`sandbox-1.4.3/market.json`) with `read_market.py`; the safety scan flagged `open(` and the user read it as read-only; met `KeyError`.
- **1.5.1 done (2026-11-19):** first real API call. `sandbox-1.5.1\fx_rates.py` calls Frankfurter (free, no key, central-bank reference rates, not trading prices) with checks for status, count and freshness. The venv was rebuilt from 1.4.2's `requirements.txt`. The user saw 200 OK (3 of 3, 0 days old) and a deliberate 422 error.
- **Fast mode since 2026-11-19 (CLAUDE.md rule):** Claude runs exercises; the user predicts, then answers 2 questions.
- **Curriculum condensed 2026-11-19** at the user's request (see DECISIONS.md): about 34 lessons remain. Keep lessons lean: short explanations, one-line commands, 2-question checks.
- **1.5.2 done (2026-11-19):** `sandbox-1.5.2` has `use_key.py` (python-dotenv, masked output) and a fake key in `.env`, typed in Notepad. `.env` was confirmed ignored by the root `.gitignore`; Claude checked without reading `.env`.
- **Note:** the user's PowerShell sometimes opens in `C:\WINDOWS\System32`. That is **not always** Administrator: on 2026-11-19 it was a normal window (writes to `C:\Windows` were "Access denied"). Correction to the earlier "System32 = admin" claim. Either way, always start exercises with an **absolute** `cd ~\AI-Program\...` instead of relative `cd ..`.
- **How to teach this user:** fast mode: Claude runs commands; the user predicts and answers 2 low-pressure questions. When the user must type something, give ONE line joined with `;`, starting with an absolute `cd`.
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
| 1.4.1 | 2026-11-19 | Exercise ✓ (scan silent; `video got more …` with two endings; diff `-the` / `+video`; restore). Check 3/3 own words ✓ | None |
| 1.4.2 | 2026-11-19 | Predictions ✓ (global can't import; only requirements.txt to Git). Check 3/3 own words ✓ | None |
| 1.4.3 | 2026-11-19 | Exercise ✓ (scan hit read as read-only; 2 up days; KeyError read bottom-up). Check 3/3 own words ✓ | Zero-based counting: reinforce in 1.5.1 |
| 1.5.1 | 2026-11-19 | Exercise ✓ (200, 3/3, fresh; 422 on a bad currency). Check 3/3 own words (Q3 "no" without the reason) | Why reference rates aren't tradable prices: revisit in the Stage 1 capstone |
| 1.5.2 | 2026-11-19 | Exercise ✓ (masked key found; `.env` ignored). Check 2/2 own words ✓ | None |

## Stage status
| Stage | Status |
|---|---|
| 0 Orientation | done |
| 1 Fundamentals | started |
| 2–6 | not started |
