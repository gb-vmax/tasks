#!/bin/bash
set -e
cd /home/user

awk '/ERROR:/ {match($0, /\[([0-9-]+ [0-9:]+)\] ERROR: (.*)/, arr); if (arr[1] && arr[2]) print arr[1] " | " arr[2]}' /home/user/app_error.log > /home/user/errors_extracted.log
awk '$0 ~ /\] ERROR:/ { sub(/^\[/, "", $1); split($0, a, "] ERROR: "); split(a[1], b, "] "); print b[1] " | " a[2] }' /home/user/app_error.log > /home/user/errors_extracted.log
cat /home/user/errors_extracted.log
