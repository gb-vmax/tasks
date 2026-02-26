FROM ubuntu:22.04

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN <<'ENDPOST'
set -eux

# Create user and home directory
useradd -m -s /bin/bash user

# Create initial project directory structure as described
install -d -m 755 /home/user/project_alpha/scripts

# Create main.py with correct content
echo 'print("Hello from main.py")' > /home/user/project_alpha/main.py
chmod 644 /home/user/project_alpha/main.py
chown user:user /home/user/project_alpha/main.py

# Create helper.sh with correct content
echo '#!/bin/bash' > /home/user/project_alpha/scripts/helper.sh
echo 'echo "Helper script"' >> /home/user/project_alpha/scripts/helper.sh
chmod 755 /home/user/project_alpha/scripts/helper.sh
chown user:user /home/user/project_alpha/scripts/helper.sh

# Set ownership for created directories
chown -R user:user /home/user/project_alpha

# Install pip and pytest
apt-get update
apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
