#!/bin/bash
set -e
cd /home/user

sed -i 's/enabled: true/enabled: false/; s/retention_days: 7/retention_days: 3/' /home/user/backup_config.yaml
sed -i '/^\[restore2\]/,/^$/s/status = "valid"/status = "invalid"/' /home/user/restore_points.toml
printf "Backup config updated: enabled false, retention_days 3\nRestore2 status updated: invalid\n" > /home/user/restore_test.log
