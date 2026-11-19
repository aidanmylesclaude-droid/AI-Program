# fx_rates.py: ask a free, no-key API for today's exchange rates (Lesson 1.5.1).
# Source: Frankfurter (api.frankfurter.dev): reference rates published by central banks.
# These are reference rates, not live trading prices. Research and education only.
# It reads from the internet and prints. It changes no files and sends no secrets.
import datetime
import requests

URL = "https://api.frankfurter.dev/v2/rates"
params = {"base": "USD", "quotes": "EUR,GBP,JPY"}

# The API call: a GET request ("please send me data").
response = requests.get(URL, params=params, timeout=10)
print("Asked for:", response.url)
print("Status code:", response.status_code)

# Check 1: did the request work? 200 means OK.
if response.status_code != 200:
    print("The API returned an error:", response.text)
    raise SystemExit(1)

# Turn the JSON text into Python data. This API returns a LIST of objects.
rates = response.json()

# Check 2: did we get everything we asked for?
print("Rates received:", len(rates), "of 3")

# Check 3: how fresh is each rate?
today = datetime.date.today()
for item in rates:
    age = (today - datetime.date.fromisoformat(item["date"])).days
    print("1", item["base"], "=", item["rate"], item["quote"], "| date:", item["date"], "| days old:", age)
