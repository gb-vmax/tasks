#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/build.log
cat > /home/user/pipeline/summarize_build.sh << 'EOF'
#!/bin/bash

LOG="/home/user/pipeline/build.log"

started=$(grep 'BUILD STARTED:' "$LOG" | sed 's/.*BUILD STARTED: //')
finished=$(grep 'BUILD FINISHED:' "$LOG" | sed 's/.*BUILD FINISHED: //')
status=$(grep 'BUILD STATUS:' "$LOG" | sed 's/.*BUILD STATUS: //')
modules_compiled=$(grep -c 'Compiled module:' "$LOG")
modules_failed=$(grep 'Compiled module:' "$LOG" | grep -c 'FAILED')
warnings=$(grep -c '^\[WARN\]' "$LOG")

echo "=== BUILD SUMMARY ==="
echo "Started:  $started"
echo "Finished: $finished"
echo "Status:   $status"
echo "Modules compiled: $modules_compiled"
echo "Modules failed:   $modules_failed"
echo "Warnings:         $warnings"
EOF
chmod +x /home/user/pipeline/summarize_build.sh
/home/user/pipeline/summarize_build.sh
