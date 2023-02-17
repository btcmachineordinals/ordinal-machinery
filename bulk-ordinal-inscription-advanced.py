import subprocess
import json
import time
import os

# Parameters
num_inscriptions = 100
start_num = 1
batch_size = 10
fee_rate = 20.0

# File to store the inscriptions
inscriptions_file = 'operators-inscriptions.json'

# Create empty inscriptions file or read existing file
if os.path.exists(inscriptions_file):
    with open(inscriptions_file, 'r') as f:
        inscriptions = json.load(f)
else:
    inscriptions = []

# Keep track of the last successful inscription number
last_successful_inscription = start_num - 1

# Loop through batches of inscriptions
while last_successful_inscription < num_inscriptions - 1:
    # Create a list of subprocesses to run in parallel
    processes = []
    for i in range(last_successful_inscription + 1, min(last_successful_inscription + 1 + batch_size, num_inscriptions + 1)):
        image_path = f'build/images/{i}.png'
        cmd = [r'F:\CORE\ORD\ord', '--cookie-file', r'F:\CORE\.cookie', 'wallet', 'inscribe', image_path, '--fee-rate', str(fee_rate)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append((p, i))

    # Wait for all subprocesses to finish
    for p, i in processes:
        p.wait()

        # Check if inscription was successful
        if p.returncode == 0:
            print(f"Inscription {i} successful.")
            inscriptions.append(f'Inscription {i}')
            last_successful_inscription = i

        # If there was an error, print the error message and exit
        else:
            print(f"Error: Inscription {i} failed with message:\n{p.stderr.read().decode()}")
            exit()

    # Wait for a bit before starting the next batch of inscriptions
    time.sleep(10)

# Write inscriptions to file
with open(inscriptions_file, 'w') as f:
    json.dump(inscriptions, f, indent=4)
