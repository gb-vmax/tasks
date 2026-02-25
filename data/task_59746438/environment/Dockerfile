FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install necessary packages
apt-get update
apt-get install -y python3 python3-pip passwd

# Install pytest
pip3 install pytest

# Ensure /home/user exists
mkdir -p /home/user

# Create group 'analytics' if it doesn't exist
if ! getent group analytics; then
    groupadd analytics
fi

# Create user 'analyst01' with home directory and set primary group to 'analytics'
if ! id -u analyst01 >/dev/null 2>&1; then
    useradd -m -d /home/analyst01 -g analytics analyst01
fi

# Also ensure analyst01 is in analytics group as a supplementary group
usermod -a -G analytics analyst01

# Create the analytics data directory
mkdir -p /home/user/team_projects/analytics_data

# Set ownership to analyst01:analytics
chown analyst01:analytics /home/user/team_projects/analytics_data

# Set permissions to 770 (drwxrwx---)
chmod 770 /home/user/team_projects/analytics_data

# Generate the permission string for the directory
perms=$(stat -c "%A" /home/user/team_projects/analytics_data)

# Write the report
echo "/home/user/team_projects/analytics_data analyst01 analytics $perms" > /home/user/analytics_permission_report.txt

# Ensure the report file is readable by all (but not writable)
chmod 644 /home/user/analytics_permission_report.txt
ENDPOST

WORKDIR /home/user
