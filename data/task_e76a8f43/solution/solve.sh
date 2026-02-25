#!/bin/bash
set -e
cd /home/user

awk -F, 'NR==1{print "department,name,salary"} NR>1{print $4","$2","$5}' /home/user/raw_data.csv > /home/user/cleaned_data.csv && echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cleaned data written to /home/user/cleaned_data.csv" >> /home/user/processing.log
