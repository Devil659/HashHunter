#!/bin/bash

# Hashunter Installer Script for Kali Linux
# Author: devil659

echo "🔧 Installing Hashunter..."

# Ensure Python3 and pip are installed
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 not found. Install it first!"
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "❌ pip3 not found. Installing..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Install required Python libraries
pip3 install tqdm rich

# Create target directory if not exists
mkdir -p ~/.hashunter/

# Copy your Python script
cp Hashunter.py ~/.hashunter/hashunter.py

# Make launcher script
echo '#!/bin/bash' > /usr/local/bin/hashunter
echo 'python3 ~/.hashunter/hashunter.py "$@"' >> /usr/local/bin/hashunter

chmod +x /usr/local/bin/hashunter

echo "✅ Hashunter installed successfully!"
echo "👉 You can now run it by typing: hashunter <hash_file> <wordlist> <output_file>"
