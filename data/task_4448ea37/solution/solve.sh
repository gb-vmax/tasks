#!/bin/bash
set -euo pipefail

# Create the uptime_audit directory
mkdir -p /home/user/uptime_audit

# Write timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Check if sshd is running
if ps -eo comm | grep -qx sshd; then
    STATUS="running"
else
    STATUS="not running"
fi

# Write log file (exactly 2 lines, no blank lines)
printf 'Timestamp: %s\nsshd status: %s\n' "$TIMESTAMP" "$STATUS" > /home/user/uptime_audit/ssh_status.log
