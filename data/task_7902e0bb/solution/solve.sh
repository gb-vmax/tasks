#!/bin/bash
set -e
cd /home/user

sort /home/user/artifact_names.txt | uniq -c | awk '{print substr($0, index($0,$2)) ": " $1}' | sort -k2,2nr -k1,1 | tee /home/user/artifacts_frequency_report.txt
