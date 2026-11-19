# Roadmap

**Order:** foundation → tools → agents. Each stage ends with a small capstone, so you prove the skill instead of just reading about it.

| Stage | Name | Goal | Capstone (proof you're ready to move on) |
|---|---|---|---|
| 0 | Orientation | Program set up and memory working | Start a fresh session and Claude knows where you left off |
| 1 | Fundamentals | Understand Claude Code, the terminal, files, Git, APIs, MCP and how agents work | Build a small script that pulls free market data from an API, run it with Claude Code, and commit it with Git |
| 2 | Second Brain | Obsidian vault that Claude actually uses | In a fresh session, Claude answers a question only the vault knows, and cites the note |
| 3 | Optimization Center | A deliberate, minimal, secure Claude Code setup | `STACK.md` complete, and every item in it has a reason and a review |
| 4 | First agents *(added)* | Build small single-purpose agents and test them | A trading-research agent that screens and explains setups (research only), with tests |
| 5 | Running agents safely *(added)* | Scheduling, monitoring, logging, cost control, recovering from errors | An agent that runs on a schedule unattended for a week, with logs and a cost report |
| 6 | Mega-agent architecture *(added)* | An orchestrator coordinating playbooks, tools and subagents for one objective | Architecture doc and a working first slice of one mega agent |

Stage 3 is **not** a free-for-all. You can review tools at any time, but you only *install* one when the current stage needs it.

## Gaps filled in your original plan
1. **Git and safety came too late.** Git is your "undo button" for the whole computer workspace, so it now comes early (Module 1.3).
2. **Security wasn't a lesson.** API keys, permissions and prompt injection come before any agent touches an outside account. *Prompt injection* means hidden instructions inside a web page or file that try to hijack an agent.
3. **No code literacy.** You don't need to become a programmer. But to judge an agent's work you need to be able to *read* basic Python and JSON, so Module 1.4 adds that.
4. **No testing of agents.** "It seemed to work once" isn't good enough. Stage 4 covers evals: repeatable tests of an agent's output.
5. **Costs.** API usage is billed per token, and subscriptions add up. Each stack decision now includes a rough monthly cost.
6. **Platform rules.** Running many accounts automatically is exactly what YouTube, TikTok and Meta's spam rules target. Each project brief now has a "rules and risks" section.
7. **Your plan ended at "understand agents".** Stages 4–6 add building agents, running them, and then scaling.
8. **On the "mega agent".** It's the right goal if you build it as one *orchestrator* plus many small, testable parts, and not as one giant prompt. We'll design it that way from the start.
