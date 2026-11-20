# market_report.py: Stage 1 capstone (1.C).
# OBJECTIVE: a weekly plain-English report on how the US dollar moved against EUR, GBP and JPY.
# EDUCATION ONLY: these are reference rates, not prices you can trade at. Nothing here is advice.
#
# What it READS:   the free Frankfurter API (no key needed).
# What it WRITES (all inside this folder, nothing else):
#   data/rates_<date>.json     the raw API answer, unchanged (evidence)
#   reports/report_<date>.md   the explained report
#   history.csv                one summary row per day (skips a day it already has)
#   run_log.txt                what happened on every run
# What it SENDS:   nothing. It never posts, emails or trades.
# Where it STOPS:  after one run, or at the first failed check.
#
# Run it with this folder's own venv:  .venv\Scripts\python.exe market_report.py
import csv
import json
import datetime
from pathlib import Path
import requests

HERE = Path(__file__).parent
BASE = "USD"
QUOTES = ["EUR", "GBP", "JPY"]
DAYS_BACK = 7
today = datetime.date.today()
start = today - datetime.timedelta(days=DAYS_BACK)

def log(level, msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {level:5} {msg}"
    print(line)
    with (HERE / "run_log.txt").open("a", encoding="utf-8") as f:
        f.write(line + "\n")

def fail(msg):
    log("ERROR", msg + " -> stopped. Nothing was saved this run.")
    raise SystemExit(1)

# ---- Step 1: fetch (tool, with checks: 1.5.1, 1.6.2)
log("INFO", f"fetching {BASE} -> {','.join(QUOTES)} from {start} to {today}")
try:
    r = requests.get("https://api.frankfurter.dev/v2/rates",
                     params={"base": BASE, "quotes": ",".join(QUOTES),
                             "from": start.isoformat(), "to": today.isoformat()},
                     timeout=10)
except requests.RequestException as e:
    fail(f"could not reach the API: {e}")
if r.status_code != 200:
    fail(f"API said {r.status_code}: {r.text[:100]}")
rows = r.json()

# ---- Step 2: check the data before trusting it
if not isinstance(rows, list) or not rows:
    fail("API returned no rows")
for row in rows:
    if not {"date", "base", "quote", "rate"} <= row.keys() or row["rate"] <= 0:
        fail(f"strange row: {row}")
series = {q: sorted((x["date"], x["rate"]) for x in rows if x["quote"] == q) for q in QUOTES}
missing = [q for q in QUOTES if len(series[q]) < 2]
if missing:
    fail(f"not enough data for {missing}")
latest = max(x["date"] for x in rows)
age = (today - datetime.date.fromisoformat(latest)).days
if age > 4:
    fail(f"newest data is {age} days old ({latest}); refusing to call it current")
log("INFO", f"checks passed: {len(rows)} rows, {len(series[QUOTES[0]])} dates, newest {latest}")

# ---- Step 3: explain (plain code, no AI needed: 1.6.1)
lines = [f"# USD weekly report, {today}",
         f"Period: {series[QUOTES[0]][0][0]} to {latest} ({len(series[QUOTES[0]])} dates with data).", ""]
summary = {"run_date": today.isoformat(), "newest_data": latest}
for q in QUOTES:
    (d0, first), (d1, last) = series[q][0], series[q][-1]
    pct = (last - first) / first * 100
    hi, lo = max(v for _, v in series[q]), min(v for _, v in series[q])
    if abs(pct) < 0.1:
        words = "barely moved"
    elif pct > 0:
        words = f"buys {pct:.2f}% MORE {q} than at the start (the dollar strengthened against {q})"
    else:
        words = f"buys {abs(pct):.2f}% LESS {q} than at the start (the dollar weakened against {q})"
    lines += [f"## {BASE} -> {q}",
              f"- {d0}: 1 {BASE} = {first} {q}",
              f"- {d1}: 1 {BASE} = {last} {q}",
              f"- Week range: {lo} to {hi}",
              f"- In plain words: 1 dollar {words}.", ""]
    summary[f"{q}_change_pct"] = round(pct, 3)
lines += ["## Read this before using these numbers",
          "- These are **reference rates** collected from central banks and similar sources,",
          "  usually published once a day. They are not live prices, and banks or brokers",
          "  charge a spread on top, so you could not trade at exactly these numbers.",
          "- A move over one week says nothing reliable about next week. No report or",
          "  system can predict currency moves or guarantee profit.",
          "- Education and research only. Not financial advice."]
report = "\n".join(lines) + "\n"

# ---- Step 4: save (evidence, report, memory: 1.6.3)
(HERE / "data").mkdir(exist_ok=True)
(HERE / "reports").mkdir(exist_ok=True)
(HERE / "data" / f"rates_{today}.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
(HERE / "reports" / f"report_{today}.md").write_text(report, encoding="utf-8")

hist = HERE / "history.csv"
already = hist.exists() and any(row["run_date"] == today.isoformat()
                                for row in csv.DictReader(hist.open(encoding="utf-8")))
if already:
    log("INFO", "history.csv already has a row for today: not adding a duplicate")
else:
    new_file = not hist.exists()
    with hist.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(summary))
        if new_file:
            w.writeheader()
        w.writerow(summary)
    log("INFO", "added today's row to history.csv")

print()
print(report)
log("INFO", "done")
