#!/bin/bash
set -euo pipefail

AUDIT_DIR="/home/user/storage_audit"
LOG_FILE="${AUDIT_DIR}/security_scan.log"

# Clear log file
> "$LOG_FILE"

# Find all files >10MB (10485760 bytes) in the audit directory
find "$AUDIT_DIR" -type f -size +10M | sort | while read -r filepath; do
    # Search for 'password' keyword (case-insensitive, treat binary as text)
    match=$(grep -ain 'password' "$filepath" 2>/dev/null | head -1) || true
    if [ -n "$match" ]; then
        line_num=$(echo "$match" | cut -d: -f1)
        echo "${filepath}: ALERT Keyword 'password' found on line ${line_num}" >> "$LOG_FILE"
    else
        echo "${filepath}: OK No sensitive keywords found." >> "$LOG_FILE"
    fi
done
