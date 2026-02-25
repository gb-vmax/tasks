#!/bin/bash
set -e
cd /home/user

cat << 'EOF' > /home/user/scripts/extract_errors.sh
#!/bin/bash
mkdir -p /home/user/errors
for logfile in /home/user/logs/app_*.log; do
    basename="$(basename "$logfile" .log)"
    grep 'ERROR' "$logfile" > "/home/user/errors/${basename}.errors" &
done
wait
EOF
chmod +x /home/user/scripts/extract_errors.sh
/home/user/scripts/extract_errors.sh
ls /home/user/logs/app_*.log | xargs -n1 basename | sort | while read fname; do count=$(wc -l < "/home/user/errors/${fname%.log}.errors"); echo "$fname: $count errors"; done > /home/user/errors/error_summary.log
cat /home/user/errors/error_summary.log
