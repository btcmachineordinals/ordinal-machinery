import subprocess
import json
import os

# Check if the JSON file exists, if not, create an empty dictionary
if os.path.isfile('operators.json'):
    with open('operators.json', 'r') as f:
        try:
            operators = json.load(f)
        except json.decoder.JSONDecodeError:
            operators = {}
else:
    operators = {}

# Find the last index of the operators dictionary and start from there
last_index = max([int(i) for i in operators.keys()], default=0)

# List of image paths to inscribe
image_paths = ["C:\\Users\\PAPO\\Documents\\Render\\BTCMACHINES\\operators\\build\\images\\{}.png".format(i) for i in range(110, 200)]

# Loop through the images and inscribe them
for index, image_path in enumerate(image_paths):
    # Inscribe the image
    subprocess.run(['F:\\CORE\\ORD\\ord', '--cookie-file', 'F:\\CORE\\.cookie', 'wallet', 'inscribe', image_path, '--fee-rate', '9.0'])
    
    # Get the output from the command
    result = subprocess.run(['F:\\CORE\\ORD\\ord', '--cookie-file', 'F:\\CORE\\.cookie', 'wallet', 'show', 'inscription', str(index + last_index + 1)], capture_output=True)
    
    # Decode the output and add it to the operators dictionary
    inscription = result.stdout.decode('utf-8').strip()
    operators[str(index + last_index + 1)] = inscription

# Sort the operators dictionary by index
sorted_operators = dict(sorted(operators.items(), key=lambda x: int(x[0])))

# Write the sorted operators dictionary to the JSON file
with open('operators.json', 'w') as f:
    json.dump(sorted_operators, f, indent=4)
