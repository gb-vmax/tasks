#!/bin/bash
set -e
cd /home/user

awk -F, 'NR==1{h=$0; for(i=1;i<=NF;i++) if($i=="value") c=i; print h; next} ($c!="" && $c ~ /^-?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/){print $0; cleaned++} {total++} END{print cleaned > "/tmp/cleaned_count.txt"; print total > "/tmp/total_count.txt"}' /home/user/data/dirty_data.csv > /home/user/data/clean_data.csv
removed=$(($(cat /tmp/total_count.txt)-$(cat /tmp/cleaned_count.txt))); remaining=$(cat /tmp/cleaned_count.txt); { echo "Removed $removed rows due to invalid or missing values"; echo "Remaining rows: $remaining"; echo "Success"; } > /home/user/data/cleaning_log.txt
cat /home/user/data/cleaning_log.txt
