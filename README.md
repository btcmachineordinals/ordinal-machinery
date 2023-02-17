BEEP BOOP🤖
Machined by PAPO https://twitter.com/papozorus
Co-founder of BTC MACHINE
https://btcmachine.com
https://discord.gg/btcmachine
https://twitter.com/btcordinal

Inscribing Images to the Bitcoin Blockchain
This Python script allows you to bulk inscribe images to the Bitcoin blockchain using ORDINALS.

Requirements
Before getting started, you will need the following:

Bitcoin Core installed and synced to the livenet
Ord installed
Python 3 installed

Getting Started
First, make sure that Bitcoin Core and ORDINALS are fully synced to the livenet. This may take some time if you are starting from scratch.

Run the following command to install the required Python packages:

pip3 install requests

In the images directory, add the images you wish to inscribe. Note that the images must be in PNG format and have a resolution of 128x128.

Open the inscribe_images.py file and modify the image_range variable to specify the range of images you wish to inscribe. For example, if you wish to inscribe images 1 to 17, set image_range = range(1, 18).

In the terminal, run the following command to start inscribing the images to the Bitcoin blockchain:

python3 inscribe_images.py

This will start the inscription process. The script will automatically create a file named inscriptions.json in the root directory of the repository to store the inscriptions.

The script will inscribe up to 10 images in parallel until all images have been inscribed. Once all images have been inscribed, the script will exit.

If you need to stop the inscription process before all images have been inscribed, you can run the script again and it will pick up where it left off. The script will check the inscriptions.json file and resume inscribing any images that have not yet been inscribed.

Checking Inscriptions
To check that your images have been inscribed to the Bitcoin blockchain, you can use a block explorer such as Blockstream.info.

Go to https://ORDINALS.com and search for the inscription using the inscription ID, it might take several minutes to update.

That's it! You have successfully inscribed NFTs to the Bitcoin blockchain using https://ORDINALS.com
