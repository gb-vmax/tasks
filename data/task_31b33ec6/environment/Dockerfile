FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -eux

# Create user and home directory
useradd -m -d /home/user user

# Install required packages
apt-get update
apt-get install -y python3-pip tar

# Install pytest
pip3 install pytest

# Set up the locales_update.tar.gz archive in /home/user

# Create a temporary staging area
mkdir -p /tmp/locales
echo 'English translation' > /tmp/locales/en_US.po
echo 'French translation' > /tmp/locales/fr_FR.po
echo 'German translation' > /tmp/locales/de_DE.po

# Create the tar.gz archive with the correct structure
cd /tmp
tar -czf locales_update.tar.gz locales

# Move the archive to the user's home directory
mv /tmp/locales_update.tar.gz /home/user/
chown user:user /home/user/locales_update.tar.gz

# Clean up
rm -rf /tmp/locales
ENDPOST

WORKDIR /home/user
