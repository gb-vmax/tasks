#!/bin/bash
set -e
cd /home/user

cat /home/user/admin/users.csv
cat << 'EOF' > /home/user/admin/gen_report.sh
#!/bin/bash

INPUT="/home/user/admin/users.csv"
OUTPUT="/home/user/admin/report.txt"

# Skip header, read all data lines
DATA=$(tail -n +2 "$INPUT")

total=$(echo "$DATA" | wc -l)
active=$(echo "$DATA" | awk -F',' '$4=="active"' | wc -l)
inactive=$(echo "$DATA" | awk -F',' '$4=="inactive"' | wc -l)

active_admins=$(echo "$DATA" | awk -F',' '$3=="admin" && $4=="active" {print $1,$2}' | sort)
active_editors=$(echo "$DATA" | awk -F',' '$3=="editor" && $4=="active" {print $1,$2}' | sort)

{
  echo "=== USER ACCOUNT REPORT ==="
  echo "Total users: $total"
  echo "Active: $active"
  echo "Inactive: $inactive"
  echo ""
  echo "Active admins:"
  if [ -n "$active_admins" ]; then
    echo "$active_admins" | while read uname email; do
      echo "  $uname ($email)"
    done
  fi
  echo ""
  echo "Active editors:"
  if [ -n "$active_editors" ]; then
    echo "$active_editors" | while read uname email; do
      echo "  $uname ($email)"
    done
  fi
} > "$OUTPUT"
EOF
chmod +x /home/user/admin/gen_report.sh
bash /home/user/admin/gen_report.sh && cat /home/user/admin/report.txt
