#!/bin/bash
set -e
cd /home/user

head -n 30 /home/user/legacy_tools/cleanup_temp_files.py
mkdir -p /home/user/legacy_data && find /home/user/legacy_data -maxdepth 1 -name '*.tmp' -delete && touch /home/user/legacy_data/temp1.tmp /home/user/legacy_data/temp2.tmp /home/user/legacy_data/temp3.tmp /home/user/legacy_data/keepme.txt /home/user/legacy_data/archive.log
mkdir -p /home/user/legacy_run/reports
python2 /home/user/legacy_tools/cleanup_temp_files.py > /home/user/legacy_run/reports/cleanup_$(date -u +%Y%m%d_%H%M%S).log
readlink -f $(ls -1 /home/user/legacy_run/reports/cleanup_*.log | sort | tail -1)
chmod 600 $(ls -1 /home/user/legacy_run/reports/cleanup_*.log | sort | tail -1)
ls -1 /home/user/legacy_data
cat /home/user/legacy_run/reports/cleanup_20260225_020059.log
