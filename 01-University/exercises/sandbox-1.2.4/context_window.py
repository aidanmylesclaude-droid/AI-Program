# context_window.py: a toy context window for Lesson 1.2.4.
# A context window is everything the model can "see" right now.
# This toy window holds only 4 lines. Real ones hold up to about a million
# tokens, and Claude Code *summarizes* old parts instead of just dropping them,
# but the problem is the same: early details can get lost.
# Read-only: it only prints.

WINDOW_SIZE = 4
rule = "RULE: always explain jargon"
conversation = [
    rule,
    "you:    what is a token?",
    "claude: a chunk of text...",
    "you:    and an API?",
    "claude: a way for programs to talk...",
    "you:    what is MCP?",
]

def show(title, window):
    print(title)
    for line in window:
        print("    ", line)

# Part 1: the rule is just an early message in the conversation.
print("=== PART 1: the rule was said once, at the start ===")
window = []
for message in conversation:
    window.append(message)
    if len(window) > WINDOW_SIZE:
        dropped = window.pop(0)
        print(f"  (window full, so the oldest line fell out: {dropped})")
show("What the model can see at the end:", window)
print("Can it still see the rule?", rule in window)
print()

# Part 2: the rule lives in a file that's loaded every time (like CLAUDE.md).
print("=== PART 2: the rule is in a file that's always loaded ===")
pinned = [rule]
window = []
for message in conversation[1:]:
    window.append(message)
    if len(pinned) + len(window) > WINDOW_SIZE:
        window.pop(0)
show("What the model can see at the end:", pinned + window)
print("Can it still see the rule?", rule in pinned + window)
