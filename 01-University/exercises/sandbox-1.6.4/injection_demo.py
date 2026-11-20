# injection_demo.py: prompt injection, least privilege and human approval, for Lesson 1.6.4.
# SAFE BY DESIGN: no tool here does anything real. Every "tool" only PRINTS what it would do.
# It does not read any .env file, send anything, or delete anything.
# Usage: python injection_demo.py           (with guardrails)
#        python injection_demo.py unsafe    (no guardrails, to see what could go wrong)
import sys
from pathlib import Path

unsafe = len(sys.argv) > 1 and sys.argv[1] == "unsafe"
email = (Path(__file__).parent / "inbox.txt").read_text(encoding="utf-8")  # UNTRUSTED data

def gullible_model(text):
    """Stands in for an LLM that has been fooled: it obeys any 'ACTION:' line it reads.
    Real models resist this much better, but no model resists it every time."""
    return [line[len("ACTION: "):] for line in text.splitlines() if line.startswith("ACTION: ")]

# Every tool that exists in the world... (all fake: they only print)
ALL_TOOLS = {"summarize", "save_note", "send_email", "delete_file"}
# ...but LEAST PRIVILEGE: this agent's job is "summarize my inbox", so it gets only these:
GRANTED = {"summarize", "save_note"}
# ...and HUMAN APPROVAL for anything that changes something:
NEEDS_APPROVAL = {"save_note"}
approved_by_human = set()  # nobody is here to approve, so this stays empty

print("MODE:", "UNSAFE (no guardrails)" if unsafe else "SAFE (least privilege + approval gate)")
print("GOAL from the user: summarize my inbox")
print()
for request in gullible_model(email):
    tool = request.split()[0]
    print(f"MODEL ASKS: {request}")
    if unsafe:
        print(f"   -> RAN (simulated): {tool}  <-- nothing checked it")
        continue
    if tool not in GRANTED:
        print(f"   -> BLOCKED by code: '{tool}' was never granted to this agent")
    elif tool in NEEDS_APPROVAL and tool not in approved_by_human:
        print(f"   -> HELD: '{tool}' needs a human's OK. None given, so it does not run")
    else:
        print(f"   -> RAN (simulated): {tool}")
