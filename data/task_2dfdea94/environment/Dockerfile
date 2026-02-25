FROM ubuntu:22.04

ENV PATH="/home/user/.local/bin:$PATH"

RUN <<'ENDPOST'
set -e

# Create user and home directory
useradd -m user
# Ensure home directory exists
mkdir -p /home/user

# Create required directories
mkdir -p /home/user/builds/output
mkdir -p /home/user/artifacts

# Create build1.tar.gz and build3.tar.gz in builds/output
echo -n "foo build content" > /home/user/builds/output/build1.tar.gz
echo -n "bar build content" > /home/user/builds/output/build2.tar.gz
echo -n "baz build content" > /home/user/builds/output/build3.tar.gz

# Create build2.tar.gz in artifacts ONLY
echo -n "old archived build" > /home/user/artifacts/build2.tar.gz

# Set permissions so user can read/write in these directories and files
chown -R user:user /home/user/builds
chown -R user:user /home/user/artifacts

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest
ENDPOST

WORKDIR /home/user
