# unattended_run.py: memory, error recovery and monitoring, for Lesson 1.6.3.
# Imagine a scheduler starts this every morning while you're asleep.
#   MEMORY:     state.json remembers past runs (the program itself forgets everything when it ends).
#   RECOVERY:   up to 3 attempts, waiting longer each time (backoff), then give up cleanly.
#   MONITORING: every event is appended to run_log.txt with a time and a level (INFO / ERROR).
# What it touches: reads the free Frankfurter API; writes state.json and run_log.txt in this folder.
# Usage: python unattended_run.py          (normal)
#        python unattended_run.py outage   (pretend the internet is down)
import sys
import json
import time
import datetime
from pathlib import Path
import requests

HERE = Path(__file__).parent
STATE = HERE / "state.json"
LOG = HERE / "run_log.txt"
outage = len(sys.argv) > 1 and sys.argv[1] == "outage"

def log(level, msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {level:5} {msg}"
    print(line)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")

# ---- MEMORY: load what earlier runs left behind
if STATE.exists():
    state = json.loads(STATE.read_text(encoding="utf-8"))
else:
    state = {"runs": 0, "last_success": None, "last_eur_rate": None}
state["runs"] += 1
log("INFO", f"run #{state['runs']} started (last success: {state['last_success']})")

# ---- RECOVERY: retry with backoff, but only a fixed number of times
rate = None
for attempt in range(1, 4):
    try:
        if outage:
            raise requests.ConnectionError("simulated outage")
        r = requests.get("https://api.frankfurter.dev/v2/rates",
                         params={"base": "USD", "quotes": "EUR"}, timeout=10)
        r.raise_for_status()
        rate = r.json()[0]["rate"]
        log("INFO", f"attempt {attempt}: OK, 1 USD = {rate} EUR")
        break
    except Exception as e:
        wait = attempt  # 1s, then 2s: "backoff"
        log("ERROR", f"attempt {attempt}: {e}")
        if attempt < 3:
            log("INFO", f"waiting {wait}s before retrying")
            time.sleep(wait)

# ---- Save memory, and make failure LOUD instead of silent
if rate is not None:
    if state["last_eur_rate"] is not None:
        log("INFO", f"change since last success: {rate - state['last_eur_rate']:+.4f}")
    state["last_success"] = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
    state["last_eur_rate"] = rate
else:
    log("ERROR", "ALERT: gave up after 3 attempts. Kept the last good data. A human should look.")

STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")
log("INFO", f"run #{state['runs']} finished")
if rate is None:
    raise SystemExit(1)
