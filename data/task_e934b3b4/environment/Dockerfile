FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install Python3 and pip, and pytest
apt-get update
apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest

# Create the user and home directory if not already present
if ! id user >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi

# Create /home/user/data_analysis directory
mkdir -p /home/user/data_analysis
chown user:user /home/user/data_analysis

# Create the three CSV files with the correct sizes and permissions
cd /home/user/data_analysis
truncate -s 15000 small_dataset.csv
truncate -s 52000 medium_dataset.csv
truncate -s 105500 large_dataset.csv
chown user:user small_dataset.csv medium_dataset.csv large_dataset.csv
chmod 644 small_dataset.csv medium_dataset.csv large_dataset.csv
ENDPOST

WORKDIR /home/user
