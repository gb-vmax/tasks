#!/bin/bash
set -e
cd /home/user

grep 'ERROR' /home/user/build_logs/pipeline.log > /home/user/build_logs/pipeline_errors.txt
wc -l < /home/user/build_logs/pipeline_errors.txt
head -n 1 /home/user/build_logs/pipeline_errors.txt
printf "Total ERROR lines extracted: 2\nFirst ERROR line: [ERROR] Failed to clone repository\n" > /home/user/build_logs/extraction_summary.txt
cat /home/user/build_logs/pipeline_errors.txt /home/user/build_logs/extraction_summary.txt
