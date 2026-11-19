# agent_loop.py: a toy agent loop for Lesson 1.2.3.
# GOAL: find the biggest lesson file.
# A real agent uses an LLM to make each decision. Here the "decisions" are
# simple if-rules, so you can see every stage of the loop.
# Read-only: it looks at files and prints. It changes nothing.
from pathlib import Path

goal = "Find the biggest lesson file"

# Places to try, in order. The first one is a deliberate mistake:
# a relative path, which only works if you're standing in the right folder (1.1.1).
candidates = [
    Path("lessons"),
    Path.home() / "AI-Program" / "01-University" / "lessons",
]
max_steps = 5  # safety limit, so the loop can never run forever

print("GOAL:", goal)
step = 0
answer = None
while answer is None and step < max_steps:
    step += 1
    if not candidates:
        print(f"[step {step}] DECIDE:  nothing left to try. Stop and report failure.")
        break
    folder = candidates.pop(0)
    print(f"[step {step}] PLAN:    list the .md files in '{folder}'")
    try:
        files = [f for f in folder.iterdir() if f.suffix == ".md"]  # ACT: use the "tool"
    except FileNotFoundError:
        print(f"[step {step}] OBSERVE: error, that folder doesn't exist (I'm standing in {Path.cwd()})")
        print(f"[step {step}] DECIDE:  it was a relative path from the wrong place. Try the next one.")
        continue
    print(f"[step {step}] OBSERVE: found {len(files)} lesson files")
    biggest = max(files, key=lambda f: f.stat().st_size)
    print(f"[step {step}] DECIDE:  biggest looks like {biggest.name}. Check it before answering.")
    size = biggest.stat().st_size  # VERIFY: look again instead of trusting the first read
    if all(size >= f.stat().st_size for f in files):
        print(f"[step {step}] VERIFY:  confirmed, nothing is bigger.")
        answer = f"{biggest.name} ({size} bytes)"

if answer:
    print("DONE:", answer)
else:
    print("STOPPED WITHOUT AN ANSWER.")
