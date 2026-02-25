FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

# Create user and home directory if not already present
if ! id -u user >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi

# Make sure /home/user exists and has correct ownership
mkdir -p /home/user
chown user:user /home/user

# Create the webapp_updates directory and required files
mkdir -p /home/user/webapp_updates
touch /home/user/webapp_updates/index.html
touch /home/user/webapp_updates/app.js
touch /home/user/webapp_updates/style.css

# (Optionally) Create the old_versions subdirectory (not required to exist)
mkdir -p /home/user/webapp_updates/old_versions

# Set permissions so user can manipulate these files/directories
chown -R user:user /home/user/webapp_updates

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest
ENDPOST

WORKDIR /home/user
