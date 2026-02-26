#!/bin/bash
set -e
cd /home/user

echo "Memory_Total_MB: $(free -m | awk '/^Mem:/ {print $2}')" > /home/user/resource_snapshot.log; echo "Memory_Used_MB: $(free -m | awk '/^Mem:/ {print $3}')" >> /home/user/resource_snapshot.log; echo "Memory_Free_MB: $(free -m | awk '/^Mem:/ {print $4}')" >> /home/user/resource_snapshot.log; echo "CPU_Count: $(nproc)" >> /home/user/resource_snapshot.log; read load1 load5 load15 _ < /proc/loadavg; echo "Load_Average_1min: $load1" >> /home/user/resource_snapshot.log; echo "Load_Average_5min: $load5" >> /home/user/resource_snapshot.log; echo "Load_Average_15min: $load15" >> /home/user/resource_snapshot.log
cat /home/user/resource_snapshot.log
