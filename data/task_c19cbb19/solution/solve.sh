#!/bin/bash
set -e
cd /home/user

awk '/^\[disk_thresholds\]/ {insec=1; next} /^\[/ {insec=0} insec && /^\/data1[[:space:]]*=/ {split($0,a,"="); gsub(/^[ \t]+|[ \t]+$/,"",a[2]); print "/data1: " a[2]} insec && /^\/backup[[:space:]]*=/ {split($0,a,"="); gsub(/^[ \t]+|[ \t]+$/,"",a[2]); x=a[2]} END{if(x) print "/backup: " x}' /home/user/storage/config.ini > /home/user/storage/threshold_summary.txt
cat /home/user/storage/threshold_summary.txt
