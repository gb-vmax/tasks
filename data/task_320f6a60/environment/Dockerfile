FROM ubuntu:22.04

ENV PATH="/home/user/.local/bin:$PATH"

RUN <<'ENDPOST'
set -eux

# Install Python3, pip, and pytest
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest

# Create user, home, and workspace structure
useradd -m -d /home/user user || true

mkdir -p /home/user/workspace
mkdir -p /home/user/projects
mkdir -p /home/user/config
mkdir -p /home/user/data

# Create target files with correct permissions and content
touch /home/user/projects/main_project.txt
chmod 600 /home/user/projects/main_project.txt
chown user:user /home/user/projects/main_project.txt

touch /home/user/config/settings.conf
chmod 640 /home/user/config/settings.conf
chown user:user /home/user/config/settings.conf

touch /home/user/data/raw_dataset.csv
chmod 750 /home/user/data/raw_dataset.csv
chown user:user /home/user/data/raw_dataset.csv

# Create symbolic links in workspace
ln -sf /home/user/projects/main_project.txt /home/user/workspace/project_link
ln -sf /home/user/config/settings.conf /home/user/workspace/config_symlink
ln -sf /home/user/data/raw_dataset.csv /home/user/workspace/data_link

# Set ownership of all created files/directories to user
chown -R user:user /home/user/workspace
chown -R user:user /home/user/projects
chown -R user:user /home/user/config
chown -R user:user /home/user/data
ENDPOST

WORKDIR /home/user
