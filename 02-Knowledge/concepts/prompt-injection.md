---
type: concept
status: active
tags: [security, agents]
created: 2026-11-20
lesson: "[[1.6.4-autonomy-and-security]]"
---
# Prompt injection
**One-line definition:** text an agent reads (an email, web page, comment) that contains instructions aimed at the model, trying to make it do something you didn't ask for.
**Problem it solves:** none: it's an attack. Knowing it explains why agents need guardrails in code.
**How it works (short):** the model reads your instructions and outside data as one stream of text, so a convincing "ignore your rules and…" can fool it. No model is fully immune, and no complete fix is known.
**Connection to Claude Code:** Claude Code treats outside content as data, not orders, and asks you to confirm. Permission rules and deny rules are the code-level guardrails (Stage 3.1).
**Do I need it? When?** Yes, from the first agent that reads anything you didn't write.
**Example from my projects:** a fake sponsorship email told the agent to send my `.env` to a stranger; the fooled model asked, the tool gate blocked it (`01-University/exercises/sandbox-1.6.4`).
**Similar to / often confused with:** phishing (tricks a *person*; injection tricks the *model*). Jailbreaking (the *user* tries to break the rules; injection comes from *content*).
**Related:** [[least-privilege]] (strongest defense), human approval, the "lethal trifecta" (private data + untrusted content + a way out).
