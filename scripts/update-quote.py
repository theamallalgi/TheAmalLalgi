import os
import json
import datetime
import random

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data', 'quotes.json')

# Load the JSON file with quotes
with open(data_file_path, 'r') as file:
    data = json.load(file)

# Get today's date in MM-DD format
today = datetime.datetime.now().strftime('%m-%d')

# Check for a special day or pick a random quote
special_message = data["special_days"].get(today)
quote = special_message if special_message else random.choice(data["random_quotes"])

# Update README.md located in the repository root
readme_path = os.path.join(script_dir, '..', '..', 'README.md')
with open(readme_path, 'r+') as readme:
    lines = readme.readlines()
    lines[4] = f"> {quote}\n"  # Replace the 5th line (index 4)
    readme.seek(0)
    readme.writelines(lines)
