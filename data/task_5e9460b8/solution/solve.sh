#!/bin/bash
set -e
cd /home/user

echo "YAML integrity_check: $(grep -m1 '^[ ]*integrity_check:' /home/user/backup/settings.yaml | sed 's/^[^:]*: *//')" > /home/user/backup/integrity_check_report.log && echo "TOML integrity_check: $(grep -m1 '^[ ]*integrity_check[ ]*=' /home/user/backup/settings.toml | sed 's/^[^=]*=[ ]*//')" >> /home/user/backup/integrity_check_report.log
cat /home/user/backup/integrity_check_report.log
