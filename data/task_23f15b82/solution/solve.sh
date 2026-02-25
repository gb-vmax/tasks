#!/bin/bash
set -e
cd /home/user

bash -c 'CPU=$(top -bn1 | grep -i "Cpu(s)" | awk "{print 100-\$8}" | head -1 | xargs printf "%.0f"); read total used <<<$(awk "/MemTotal|MemAvailable/ {print int(\$2/1024)}" /proc/meminfo | tr "\n" " "); used=$((total-used)); perc=$((used*100/total)); printf "CPU Usage: %s%%\nMemory Usage: %s%% (%s MiB / %s MiB)\n" "$CPU" "$perc" "$used" "$total" > /home/user/capacity_report.txt'
cat /home/user/capacity_report.txt
