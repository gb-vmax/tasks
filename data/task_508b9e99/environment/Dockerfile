FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Create user and set up home directory
useradd -m user

# Ensure directory structure exists
mkdir -p /home/user/database/logs

# Create a non-empty query.log file
echo "SELECT * FROM table WHERE id = 1;" > /home/user/database/logs/query.log

# Set ownership to user:user for all home files
chown -R user:user /home/user

# Ensure permissions for /home/user, /home/user/database, /home/user/database/logs
chmod 700 /home/user
chmod 700 /home/user/database
chmod 700 /home/user/database/logs

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest
ENDPOST

WORKDIR /home/user
