FROM ubuntu:22.04

ENV PATH=/home/user/backup_verification/venv/bin:$PATH

RUN <<'ENDPOST'
set -eux

    # Create user home directory and backup_verification directory
    mkdir -p /home/user/backup_verification

    # Ensure permissions for user access
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/backup_verification

    # Install Python 3, venv, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-venv python3-pip

    # Create a standard Python venv in the correct location
    cd /home/user/backup_verification
    python3 -m venv venv

    # Install pytest globally (for test runner)
    pip3 install pytest

    # Create check_backup.py that prints "Backup OK"
    cat > /home/user/backup_verification/check_backup.py <<'EOF'
import sys
if __name__ == "__main__":
    print("Backup OK")
EOF
    chmod 644 /home/user/backup_verification/check_backup.py

    # Create a valid backup.tar.gz (minimal tarball)
    cd /home/user/backup_verification
    echo "dummy data" > dummy.txt
    tar czf backup.tar.gz dummy.txt
    rm dummy.txt
    chmod 644 /home/user/backup_verification/backup.tar.gz

    # Create verify.log with a single line "Backup OK"
    echo "Backup OK" > /home/user/backup_verification/verify.log
    chmod 644 /home/user/backup_verification/verify.log

    # Make sure venv/bin/python is executable
    chmod +x /home/user/backup_verification/venv/bin/python

    # Ensure all files and venv are owned by user
    chown -R 1000:1000 /home/user/backup_verification
ENDPOST

WORKDIR /home/user
