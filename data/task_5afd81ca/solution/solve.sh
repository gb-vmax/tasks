#!/bin/bash
set -e
cd /home/user

awk -F',' '$2=="ERROR"' /home/user/server_data.csv > /tmp/new_errors.csv && N=$(wc -l < /tmp/new_errors.csv); if [ "$N" -eq 0 ]; then echo "No new error lines to append."; else cat /tmp/new_errors.csv >> /home/user/error_log.txt; echo "Appended $N lines to /home/user/error_log.txt"; fi
