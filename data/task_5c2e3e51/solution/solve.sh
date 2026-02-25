#!/bin/bash
set -e
cd /home/user

(
cd /home/user/backup_logs &&
ls -1t backup_*.log | head -5 | sort | while read f; do
  grep "Database backup completed: customer_data" "$f" | tail -1
done | awk '
BEGIN{
  print "DATE_TIME | STATUS | DURATION"
}
{
  # Example line: [2024-06-18 01:43:00] INFO: Database backup completed: customer_data (Duration: 00:12:03) - STATUS: SUCCESS
  match($0, /^\[([0-9-]+ [0-9:]+)\].*Duration: ([0-9:]+)\) - STATUS: (SUCCESS|FAILURE)$/, arr)
  if (arr[1] && arr[2] && arr[3]) {
    print arr[1] " | " arr[3] " | " arr[2]
  }
}' > /home/user/backup_summary/backup_status_report.txt
(printf "DATE_TIME | STATUS | DURATION\n" > /home/user/backup_summary/backup_status_report.txt && for f in $(ls -1t /home/user/backup_logs/backup_*.log | head -5 | sort); do grep "Database backup completed: customer_data" "$f" | tail -1; done | awk 'match($0, /^\[([0-9\-]+ [0-9:]+)\].*Duration: ([0-9:]+)\) - STATUS: (SUCCESS|FAILURE)$/, arr) {print arr[1] " | " arr[3] " | " arr[2]}' >> /home/user/backup_summary/backup_status_report.txt)
(printf "DATE_TIME | STATUS | DURATION\n" > /home/user/backup_summary/backup_status_report.txt && for f in $(ls -1t /home/user/backup_logs/backup_*.log | head -5 | sort); do grep "Database backup completed: customer_data" "$f" | tail -1; done | sed -n 's/^\[\([^]]*\)\].*Duration: \([0-9:]*\)).*STATUS: \(SUCCESS\|FAILURE\)$/\1 | \3 | \2/p' >> /home/user/backup_summary/backup_status_report.txt)
cat /home/user/backup_summary/backup_status_report.txt
