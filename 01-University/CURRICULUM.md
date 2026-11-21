# Curriculum checklist

Status key: `[ ]` not started · `[~]` in progress · `[x]` done.
Each lesson's full text is in `lessons/` once it has been taught. File names use the ID, for example `1.1.1-files-folders-paths.md`.
Lessons are written as we reach them, so they reflect the current tools and your progress.

## Stage 0: Orientation
- [x] 0.1 Program setup: folder, CLAUDE.md, roadmap, memory

## Stage 1: Fundamentals
### Module 1.1: Your computer as a workspace *(your top priority)*
- [x] 1.1.1 Files, folders and paths, and why we didn't build this in System32
- [x] 1.1.2 What the terminal is: PowerShell vs Command Prompt vs bash
- [x] 1.1.3 Moving around: `pwd`, `cd`, `ls`, relative vs absolute paths
- [x] 1.1.4 Creating, copying, moving and safely deleting files
- [x] 1.1.5 File types you'll meet: `.md`, `.txt`, `.json`, `.yaml`, `.env`, `.py`
- [x] 1.1.6 How Claude Code runs commands for you, and how to read what it ran
- [x] 1.1.7 Instruction files: project `CLAUDE.md` vs global `~/.claude/CLAUDE.md` vs settings files
- [x] 1.1.8 Keeping projects separate: one folder, one CLAUDE.md, and its own settings and secrets

### Module 1.2: Claude and Claude Code
- [x] 1.2.1 What an LLM is: tokens, training and prediction, and what we can't see inside it
- [x] 1.2.2 Claude chat vs Claude Code vs autocomplete coding assistants
- [x] 1.2.3 The agent loop: read, plan, act with tools, observe, repeat
- [x] 1.2.4 Context windows, and why a new session forgets (and how this program fixes that)
- [x] 1.2.5 Permissions and modes: what Claude may do on your computer
- [x] 1.2.6 Getting great results: clear requests, plan mode, asking it to verify
- [x] 1.2.7 Limits: hallucination, outdated knowledge, overconfidence, and how to catch them

### Module 1.3: Your safety net, Git and GitHub
- [x] 1.3.1 What version control is. Install Git and make your first commit.
- [x] 1.3.2 Undoing mistakes: diff, restore, revert
- [x] 1.3.3 GitHub: remotes, private repos, pushing a backup
- [x] 1.3.4 `.gitignore` and keeping secrets out of history

### Module 1.4: Minimum code literacy *(added)*
- [x] 1.4.1 Reading a Python script line by line
- [x] 1.4.2 Packages, virtual environments and `pip`, so projects don't share libraries
- [x] 1.4.3 JSON: the language APIs speak

### Module 1.5: The ecosystem, one concept at a time
Each lesson answers: what it is, what it does, why it exists, how it works, how it connects to Claude Code, when you'd need it, and an example from your projects.
- [x] 1.5.1 APIs, with a hands-on call to a free market-data API
- [x] 1.5.2 API keys, secrets and `.env` files
- [x] 1.5.3 Connecting Claude to outside apps: MCP, connectors, integrations and plugins *(merged: old 1.5.3 + 1.5.4)*
- [x] 1.5.4 Customizing Claude Code: skills, slash commands and hooks *(merged: old 1.5.5 + 1.5.6)*
- [x] 1.5.5 Delegation, models and cost: subagents, picking a model, routing work *(merged: old 1.5.7 + 1.5.9)*
- [x] 1.5.6 Recap: memory systems, and the "you don't need this" list *(merged: old 1.5.8 + 1.5.11; mostly review of 1.1.7 and 1.2.4)*

### Module 1.6: How autonomous agents work *(condensed from 8 lessons to 4)*
- [x] 1.6.1 Chatbot → assistant → automated workflow (schedulers, n8n/Zapier) → agent → multi-agent system *(includes old 1.5.10)*
- [x] 1.6.2 Planning and tools: objective to task list, chaining tools and outside data *(old 1.6.2 + 1.6.3)*
- [x] 1.6.3 Running without supervision: memory between sessions, error recovery, monitoring *(old 1.6.4–1.6.6; builds on 1.2.3–1.2.4)*
- [x] 1.6.4 Autonomy and security: reference architecture, prompt injection, least privilege, human approval steps *(old 1.6.7 + 1.6.8; security kept in full)*

### Stage 1 capstone
- [x] 1.C Market-data script: API call, saved results, explained output, committed to Git

## Stage 2: Second Brain (Obsidian) *(condensed from 7 to 4)*
- [x] 2.1 What Obsidian is, why it works as a second brain, and opening *this folder* as the vault (click by click)
- [x] 2.2 How Claude Code reads the vault: direct file access vs Obsidian MCP/plugins (pros, cons, setup)
- [x] 2.3 Organizing notes: note types (permanent, reference, active, temporary, long-term), links, tags, properties, templates
- [x] 2.C Maintenance routine, plus proof test: a fresh session answers from the vault and cites the note

## Stage 3: Optimization Center *(condensed from 9 to 5: hands-on setup, no re-teaching of Module 1.5)*
- [x] 3.1 Settings, permissions and security hardening (including a `deny` rule for `.env`)
- [x] 3.2 Instruction files, memory, skills, hooks and slash commands: set up only what you need
- [x] 3.3 MCP servers, connectors and APIs: choose and connect
- [x] 3.4 Dev, test and debug tools, subagents and automation: what to adopt and what to skip
- [x] 3.C Stack advisor and tool research desk as repeatable processes; `STACK.md` finalized

## Stage 4: First agents
- [x] 4.1 Claude Agent SDK vs Claude Code headless mode vs no-code tools
*(Changed 2026-11-20: the first agent is the **content agent**; the trading agent is parked.)*
- [x] 4.2 Design the content agent v1: one job, its tools, what it may never do (platform rules, AI disclosure, approval before anything is posted)
- [~] 4.3 Build: a single-purpose content research agent (Claude API + tools in Python; needs the user's Console account + API key first)
- [ ] 4.4 Evals: testing an agent's outputs
- [ ] 4.5 Costs: measuring tokens and dollars
- [ ] 4.C Content agent v1: drafts only, nothing published without your approval

## Stage 5: Running agents safely
- [ ] 5.1 Scheduling and triggers
- [ ] 5.2 Logging and monitoring
- [ ] 5.3 Error recovery and retries
- [ ] 5.4 Human-in-the-loop approvals
- [ ] 5.C One week unattended, with a report

## Stage 6: Mega-agent architecture
- [ ] 6.1 Orchestrator plus playbooks plus tools plus subagents
- [ ] 6.2 Shared memory and state
- [ ] 6.3 Choose the first objective and design it
- [ ] 6.C First working slice
