FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip (required for pytest)
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create users alice and bob, and a regular user 'user'
    useradd -m -s /bin/bash alice
    useradd -m -s /bin/bash bob
    useradd -m -s /bin/bash user

    # Create crontab directory with correct permissions
    mkdir -p /var/spool/cron/crontabs
    chmod 1730 /var/spool/cron/crontabs  # sticky bit, group write, owner rwx, others --x (standard for crontab dirs)

    # Create alice's crontab with correct content, permissions and ownership
    cat > /var/spool/cron/crontabs/alice <<EOF
0 5 * * 1 /home/alice/backup.sh
15 14 1 * * /usr/bin/python3 /home/alice/scripts/cleanup.py
# This is a comment and should be ignored
EOF
    chown alice: /var/spool/cron/crontabs/alice
    chmod 600 /var/spool/cron/crontabs/alice

    # Create bob's crontab with correct content, permissions and ownership
    cat > /var/spool/cron/crontabs/bob <<EOF
*/10 * * * * /home/bob/report.sh
EOF
    chown bob: /var/spool/cron/crontabs/bob
    chmod 600 /var/spool/cron/crontabs/bob

    # Create alice and bob home subdirectories for context (not strictly required but realistic)
    mkdir -p /home/alice/scripts
    mkdir -p /home/bob
    touch /home/alice/backup.sh
    touch /home/alice/scripts/cleanup.py
    touch /home/bob/report.sh
    chown -R alice: /home/alice
    chown -R bob: /home/bob
    chmod 700 /home/alice
    chmod 700 /home/bob

    # Create /home/user directory if not already created
    mkdir -p /home/user
    chown user: /home/user
    chmod 700 /home/user
ENDPOST

WORKDIR /home/user
