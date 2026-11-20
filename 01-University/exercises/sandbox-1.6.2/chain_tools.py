# chain_tools.py: planning and tool chaining, for Lesson 1.6.2.
# OBJECTIVE: "Write a short report: what is 100 USD worth in a few currencies today?"
# In a real agent, an LLM would write the plan and choose each tool.
# Here the plan is written out by hand so you can see every link in the chain.
# What it touches: reads from the free Frankfurter API (no key); writes ONE file,
# report.txt, in this folder, and only if every earlier step passed its check.
import sys
import datetime
from pathlib import Path
import requests

# ---- The tool menu. Real agents get tools described just like this:
# ---- a name, a plain-English description, and the inputs it needs.
TOOLS = {
    "fetch_rates":  "Get today's reference rates from the Frankfurter API. Inputs: base, quotes",
    "convert":      "Turn rates into 'amount in each currency'. Inputs: rates, amount",
    "save_report":  "Write lines of text to report.txt in this folder. Inputs: lines",
}

def fetch_rates(base, quotes):
    r = requests.get("https://api.frankfurter.dev/v2/rates",
                     params={"base": base, "quotes": quotes}, timeout=10)
    if r.status_code != 200:
        return None, f"API said {r.status_code}: {r.text[:80]}"
    return r.json(), None

def convert(rates, amount):
    return [f"{amount} {x['base']} = {round(amount * x['rate'], 2)} {x['quote']} (rate date {x['date']})"
            for x in rates], None

def save_report(lines):
    path = Path(__file__).parent / "report.txt"
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    path.write_text(f"Report made {stamp}\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return str(path), None

# ---- The plan: objective -> ordered tasks, each with a "done" check.
quotes = sys.argv[1] if len(sys.argv) > 1 else "EUR,GBP,JPY"
wanted = len(quotes.split(","))
print("OBJECTIVE: what is 100 USD worth in", quotes, "today?")
print("TOOLS AVAILABLE:", ", ".join(TOOLS))
print("PLAN:")
print("  1. fetch_rates  -> done when: got", wanted, "rates")
print("  2. convert      -> done when: one line per rate")
print("  3. save_report  -> done when: report.txt exists")
print()

# ---- Run the chain. Each step's OUTPUT is the next step's INPUT.
rates, err = fetch_rates("USD", quotes)
if err or len(rates) != wanted:
    print("[1] fetch_rates  FAILED:", err or f"got {len(rates)} of {wanted} rates")
    print("STOP: later steps need this data, so they are skipped. report.txt was not touched.")
    raise SystemExit(1)
print("[1] fetch_rates  OK:", len(rates), "rates")

lines, err = convert(rates, 100)
if err or len(lines) != len(rates):
    print("[2] convert      FAILED"); raise SystemExit(1)
print("[2] convert      OK:", len(lines), "lines")

path, err = save_report(lines)
if err or not Path(path).exists():
    print("[3] save_report  FAILED"); raise SystemExit(1)
print("[3] save_report  OK:", path)
print()
print(Path(path).read_text(encoding="utf-8"))
