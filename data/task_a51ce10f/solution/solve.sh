#!/bin/bash
set -e
cd /home/user

find /home/user/applogs -type f -name "*.log" | head -20 && echo "---" && ls /home/user/applogs
find /home/user/applogs -type f -name "*.log" -exec ls -la {} \;
mkdir -p /home/user/backup/archive/
find /home/user/applogs -type f -name "*.log" -size +10k | xargs -I {} cp {} /home/user/backup/archive/
ls -la /home/user/backup/archive/
find /home/user/backup/archive/ -type f -name "*.log" | xargs md5sum | sed 's|  .*/|  |' | sort -k2 > /home/user/backup/manifest.txt
N=$(wc -l < /home/user/backup/manifest.txt) && printf "TOTAL FILES: %d" "$N" >> /home/user/backup/manifest.txt
cat /home/user/backup/manifest.txt
xxd /home/user/backup/manifest.txt | tail -3
od -c /home/user/backup/manifest.txt | tail -3
