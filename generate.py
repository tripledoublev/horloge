# Build: python3 generate.py
# Looks into horloge.json to find how many artworks there are
# Generates a directory for each artwork and copies template.html into it as index.html

import os
import json
import shutil

# Path to your JSON file and template
json_file_path = 'horloge.json'
template_file_path = 'template.html'

# Load JSON file to get the count of keys
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Iterate over keys and create directories
for key in data.keys():
    directory_path = os.path.join(os.getcwd(), key)

    # Create directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    # Copy template.html to directory as index.html
    shutil.copy(template_file_path, os.path.join(directory_path, 'index.html'))

print("Directories created and files copied.")
