#!/bin/bash
set -e
cd /home/user

{ mpstat 1 1 | awk '/Average/ {usage=100-$NF; printf "CPU Usage: %.1f%%\n", usage}'; free -m | awk '/^Mem:/ {printf "Available RAM: %d MB\n", $7}'; df -B1 /home | awk 'NR==2 {printf "Free Disk Space in /home: %.2f GB\n", $4/1024/1024/1024}'; } > /home/user/ml_resource_snapshot.log
{ read cpu a b c d rest < /proc/stat; total1=$((a+b+c+d)); idle1=$d; sleep 1; read cpu a2 b2 c2 d2 rest2 < /proc/stat; total2=$((a2+b2+c2+d2)); idle2=$d2; cpu_usage=$(awk "BEGIN {printf \"%.1f\", 100 - (($idle2 - $idle1) * 100 / ($total2 - $total1))}"); echo "CPU Usage: $cpu_usage%"; free -m | awk '/^Mem:/ {printf "Available RAM: %d MB\n", $7}'; df -B1 /home | awk 'NR==2 {printf "Free Disk Space in /home: %.2f GB\n", $4/1024/1024/1024}'; } > /home/user/ml_resource_snapshot.log
cat /home/user/ml_resource_snapshot.log
