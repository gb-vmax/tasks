FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -e

# Create user and set up home directory
useradd -m user
mkdir -p /home/user/data/raw_images
mkdir -p /home/user/data/old
mkdir -p /home/user/data/temp

# Create files in raw_images
touch /home/user/data/raw_images/cats_001.jpg
touch /home/user/data/raw_images/cats_002.jpg
touch /home/user/data/raw_images/dogs_001.jpg
touch /home/user/data/raw_images/birds_001.jpg
touch /home/user/data/raw_images/testpic.jpg

# Create files in old directory
touch /home/user/data/old/notes.txt
touch /home/user/data/old/oldfile.csv

# Create files in temp directory
touch /home/user/data/temp/tempdata1.txt
touch /home/user/data/temp/tempdata2.csv

# Set permissions: all files and dirs owned by user, readable and writable
chown -R user:user /home/user/data
chmod -R u+rwX,go+rX /home/user/data

# Install Python and pip
apt-get update
apt-get install -y python3 python3-pip

# Install pytest
pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
