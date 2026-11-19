# use_key.py: read an API key from .env without ever showing it (Lesson 1.5.2).
# It reads .env in this folder and prints only WHETHER a key was found.
# It changes no files and uses no internet. The key in this lesson is FAKE.
import os
from dotenv import load_dotenv

# Copy the NAME=value lines from .env into this program's environment.
load_dotenv()

# Read one value by name. If it's missing, this gives None instead of crashing.
key = os.environ.get("MARKET_API_KEY")

if not key:
    print("No MARKET_API_KEY found. Create a .env file with a line like: MARKET_API_KEY=...")
    raise SystemExit(1)

# Never print the whole key. Show just enough to confirm it's the right one.
print("Key found. Length:", len(key), "| ends with: ..." + key[-4:])
print("A real script would now send it to the API, usually in a request header.")
