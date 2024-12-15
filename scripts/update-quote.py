import json
import datetime
import random

# Load the JSON file with quotes
with open('data/quotes.json', 'r') as file:
    data = json.load(file)

# Get today's date in MM-DD format
today = datetime.datetime.now().strftime('%m-%d')

# Check for a special day or pick a random quote
special_message = data["special_days"].get(today)
quote = special_message if special_message else random.choice(data["random_quotes"])

# Update README.md
with open('README.md', 'r+') as readme:
    lines = readme.readlines()
    lines[4] = f"> {quote}\n"  # Replace the 5th line (index 4)
    readme.seek(0)
    readme.writelines(lines)
