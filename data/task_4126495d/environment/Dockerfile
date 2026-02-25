FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install python3-pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install --no-cache-dir pytest

# Create user 'user' with home directory /home/user and group 'user'
groupadd -g 1000 user
useradd -m -u 1000 -g user user

# Create /home/user/security_audit and set ownership
install -d -o user -g user /home/user/security_audit

# Create the files with correct permissions, ownership, and content
touch /home/user/security_audit/readme.txt
touch /home/user/security_audit/report.log
touch /home/user/security_audit/confidential.md

chown user:user /home/user/security_audit/readme.txt
chown user:user /home/user/security_audit/report.log
chown user:user /home/user/security_audit/confidential.md

chmod 644 /home/user/security_audit/readme.txt
chmod 600 /home/user/security_audit/report.log
chmod 400 /home/user/security_audit/confidential.md

# Create the subdirectory archive (ignore its contents for the task)
install -d -o user -g user /home/user/security_audit/archive
ENDPOST

WORKDIR /home/user
