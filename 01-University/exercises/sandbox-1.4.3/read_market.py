# read_market.py: read made-up market data from JSON (Lesson 1.4.3).
# It reads market.json in this folder and prints a summary.
# It changes no files and uses no internet. The prices are fake.
import json

# Open market.json for READING, and parse the JSON text into Python data.
with open("market.json", encoding="utf-8") as f:
    data = json.load(f)

print("Symbol:", data["symbol"])
print("Source:", data["source"])
print("Number of days:", len(data["bars"]))

# "bars" is a list; [0] is the first item in it.
first = data["bars"][0]
print("First day:", first["date"], "closed at", first["close"])

# Go through every day and say whether it closed up or down.
for bar in data["bars"]:
    change = round(bar["close"] - bar["open"], 2)
    if change > 0:
        direction = "up"
    else:
        direction = "down"
    print(bar["date"], direction, change)

# null in JSON becomes None in Python.
print("More pages?", data["next_page"])
