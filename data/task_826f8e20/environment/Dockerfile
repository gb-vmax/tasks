FROM endless-base:latest

RUN <<'ENDPOST'
set -eux

# Install Python3, pip, and pytest
apt-get update
apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest

# Create project directory and config files
mkdir -p /home/user/my_python_project

# Create empty or placeholder settings.yaml and config.toml
touch /home/user/my_python_project/settings.yaml
touch /home/user/my_python_project/config.toml

# Set permissions: ensure user can write to the directory and files
chmod 755 /home/user/my_python_project
chmod 644 /home/user/my_python_project/settings.yaml /home/user/my_python_project/config.toml
ENDPOST

WORKDIR /home/user
