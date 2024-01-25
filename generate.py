# Build: python3 generate.py
# Looks into horloge.json to find how many artworks there are
# Generates a directory for each artwork and copies template.html into it as index.html

import os
import json
import shutil
import base64

# Path to your JSON file and template
json_file_path = 'horloge.json'
template_file_path = 'template.html'

# Load JSON file to get the count of keys
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Get the total number of artworks
total_artworks = len(data)

# Iterate over keys and create directories
for key, encoded_artwork_data in data.items():
    directory_path = os.path.join(os.getcwd(), key)

    # Create directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    # Copy template.html to directory as index.html
    shutil.copy(template_file_path, os.path.join(directory_path, 'index.html'))

    # Decode and parse the artwork data
    decoded_json = base64.b64decode(encoded_artwork_data.split(',')[1]).decode('utf-8')
    artwork_data = json.loads(decoded_json)

    # Add total artwork count to the artwork data
    artwork_data_with_count = artwork_data.copy()
    artwork_data_with_count['total_artworks'] = total_artworks

    # Re-encode the modified artwork data to Base64
    modified_encoded_artwork_data = base64.b64encode(json.dumps(artwork_data_with_count).encode('utf-8')).decode('utf-8')

    # Create a JSON file for the specific artwork
    with open(os.path.join(directory_path, 'data.json'), 'w') as json_file:
        json.dump({key: modified_encoded_artwork_data}, json_file)

print("Directories created, files copied, and JSON files generated.")