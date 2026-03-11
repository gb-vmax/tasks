#!/bin/bash
set -e
cd /home/user

ls /home/user/pipeline_data
du -sh /home/user/pipeline_data/*/ | sort -rh > /home/user/disk_report.txt
cat /home/user/disk_report.txt
du -sh /home/user/pipeline_data/* | sort -rh > /home/user/disk_report.txt
cat /home/user/disk_report.txt
