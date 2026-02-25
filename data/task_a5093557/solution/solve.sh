#!/bin/bash
set -e
cd /home/user

python3 -m venv /home/user/backup_verification/venv
/home/user/backup_verification/venv/bin/python /home/user/backup_verification/check_backup.py | grep '^Backup OK$' >> /home/user/backup_verification/verify.log
tail -n 1 /home/user/backup_verification/verify.log
