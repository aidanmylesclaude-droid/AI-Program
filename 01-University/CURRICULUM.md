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
- [ ] 1.4.1 Reading a Python script line by line
- [ ] 1.4.2 Packages, virtual environments and `pip`, so projects don't share libraries
- [ ] 1.4.3 JSON: the language APIs speak

### Module 1.5: The ecosystem, one concept at a time
Each lesson answers: what it is, what it does, why it exists, how it works, how it connects to Claude Code, when you'd need it, and an example from your projects.
- [ ] 1.5.1 APIs, with a hands-on call to a free market-data API
- [ ] 1.5.2 API keys, secrets and `.env` files
- [ ] 1.5.3 MCP (Model Context Protocol): connecting Claude to outside apps
- [ ] 1.5.4 Connectors vs integrations vs plugins vs MCP servers: what's the difference?
- [ ] 1.5.5 Skills and slash commands: reusable playbooks
- [ ] 1.5.6 Hooks: automatic rules the harness enforces
- [ ] 1.5.7 Subagents: when to delegate, and when it just wastes money
- [ ] 1.5.8 Memory systems: CLAUDE.md, auto-memory, vaults, databases
- [ ] 1.5.9 Models and orchestration: picking a model, routing work, cost
- [ ] 1.5.10 Automation tools (schedulers, n8n/Zapier-style tools) vs agents
- [ ] 1.5.11 The "you don't need this" list

### Module 1.6: How autonomous agents work
- [ ] 1.6.1 Chatbot → assistant → workflow → agent → multi-agent system
- [ ] 1.6.2 From objective to task list: planning
- [ ] 1.6.3 Tools, outside information, and chaining tools together
- [ ] 1.6.4 Remembering between sessions
- [ ] 1.6.5 Noticing and recovering from errors
- [ ] 1.6.6 Monitoring and finishing without supervision
- [ ] 1.6.7 What makes an agent truly autonomous, plus a reference architecture
- [ ] 1.6.8 Security for agents: prompt injection, least privilege, human approval steps

### Stage 1 capstone
- [ ] 1.C Market-data script: API call, saved results, explained output, committed to Git

## Stage 2: Second Brain (Obsidian)
- [ ] 2.1 What Obsidian is and why it works as a second brain
- [ ] 2.2 Install it and open *this folder* as the vault (click by click)
- [ ] 2.3 How Claude Code reads the vault: direct file access vs Obsidian MCP/plugins (pros, cons, setup)
- [ ] 2.4 Note types: permanent instructions, reference, active context, temporary, long-term
- [ ] 2.5 Links, tags, properties and templates
- [ ] 2.6 Maintenance: weekly review, finding duplicates, archiving stale notes
- [ ] 2.C Proof test: a fresh session answers from the vault and cites the note

## Stage 3: Optimization Center
- [ ] 3.1 Review: settings and permissions
- [ ] 3.2 Review: instruction files and memory
- [ ] 3.3 Review: skills, hooks and slash commands
- [ ] 3.4 Review: MCP servers, connectors, APIs
- [ ] 3.5 Review: GitHub, open-source tools, dev, test and debug tools
- [ ] 3.6 Review: subagents, orchestration, automation frameworks
- [ ] 3.7 Security hardening
- [ ] 3.8 Using the stack advisor and tool research desk (repeatable processes)
- [ ] 3.C `STACK.md` finalized

## Stage 4: First agents
- [ ] 4.1 Claude Agent SDK vs Claude Code headless mode vs no-code tools
- [ ] 4.2 Bring in the earlier trading-research project and review it
- [ ] 4.3 Build: a single-purpose research agent
- [ ] 4.4 Evals: testing an agent's outputs
- [ ] 4.5 Costs: measuring tokens and dollars
- [ ] 4.C Trading research agent v1 (research and education only)

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
