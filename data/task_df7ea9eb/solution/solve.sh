#!/bin/bash
set -e
cd /home/user

cat /home/user/backups/backup_nightly.log
grep '^\[[0-9-]* [0-9:]*\] COMPLETED ' /home/user/backups/backup_nightly.log | sed 's/^\[\([0-9-]* [0-9:]*\)\] COMPLETED \(.*\)$/Job: \2 | Completed at: \1/' > /home/user/backups/archive_summary.txt
cat /home/user/backups/archive_summary.txt
