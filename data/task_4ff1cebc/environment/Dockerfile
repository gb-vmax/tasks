FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install Python3, pip, and tar (tar is installed by default, but ensure it's present)
apt-get update
apt-get install -y python3 python3-pip tar

# Install pytest for testing
pip3 install pytest

# Create user and home directory if not present
if ! id user >/dev/null 2>&1; then
    useradd -m -d /home/user user
fi

# Ensure ownership and permissions
mkdir -p /home/user/logs
mkdir -p /home/user/diagnostics
chown -R user:user /home/user
chmod 700 /home/user
chmod 700 /home/user/logs
chmod 700 /home/user/diagnostics

# Create the log files with specified content
echo -n "System log data\n" > /home/user/logs/syslog.txt
echo -n "Authentication log data\n" > /home/user/logs/auth.log
echo -n "Kernel log data\n" > /home/user/logs/kernel.log

# Set ownership to user for all created files
chown user:user /home/user/logs/syslog.txt
chown user:user /home/user/logs/auth.log
chown user:user /home/user/logs/kernel.log

# Set permissions for the files (rw for user only)
chmod 600 /home/user/logs/syslog.txt
chmod 600 /home/user/logs/auth.log
chmod 600 /home/user/logs/kernel.log
ENDPOST

WORKDIR /home/user
