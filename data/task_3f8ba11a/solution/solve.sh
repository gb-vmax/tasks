#!/bin/bash
set -e
cd /home/user

awk 'END{print NR}' /home/user/cicd_logs/build_log_2024-06-01.txt /home/user/cicd_logs/build_log_2024-06-02.txt
grep -c "BUILD FAILED" /home/user/cicd_logs/build_log_2024-06-01.txt /home/user/cicd_logs/build_log_2024-06-02.txt
grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/.*BUILD FAILED:[ ]*\(.*\)$/\1/' | sort | uniq -c | sort -nr
awk 'FNR==1{date=gensub(/.*build_log_([0-9-]+)\.txt.*/,"\\1","g",FILENAME)} /BUILD FAILED:/ {msg=gensub(/.*BUILD FAILED:[ ]*/,"","g"); if(!seen[msg]++){print date " - " msg}}' /home/user/cicd_logs/build_log_2024-06-01.txt /home/user/cicd_logs/build_log_2024-06-02.txt
grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt | sed 's/^/2024-06-01 - /' ; grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/^/2024-06-02 - /'
(grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt | sed 's/^.*: BUILD FAILED: /2024-06-01 - /'; grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/^.*: BUILD FAILED: /2024-06-02 - /') | awk -F' - ' '!seen[$2]++{print $1 " - " $2}'
(grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt | sed 's/^.*BUILD FAILED: /2024-06-01 - /'; grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/^.*BUILD FAILED: /2024-06-02 - /') | awk -F' - ' '!seen[$2]++{print $1 " - " $2}'
(grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt | sed 's/.*BUILD FAILED:[ ]*/2024-06-01 - /'; grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/.*BUILD FAILED:[ ]*/2024-06-02 - /') | awk -F' - ' '!seen[$2]++{print $1 " - " $2}'
(grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-01.txt | sed 's/.*BUILD FAILED:[ ]*/2024-06-01|||/'; grep "BUILD FAILED:" /home/user/cicd_logs/build_log_2024-06-02.txt | sed 's/.*BUILD FAILED:[ ]*/2024-06-02|||/') | awk -F'\|\|\|' '!seen[$2]++{print $1 " - " $2}'
printf "Total builds: 11\nFailed builds: 6\nMost common failure: DependencyError - missing package xyz\n\nUnique failures:\n2024-06-01 - DependencyError - missing package xyz\n2024-06-01 - TestError - test suite failed\n2024-06-02 - TimeoutError - build step exceeded time limit\n" > /home/user/cicd_logs/build_failure_summary.txt
cat /home/user/cicd_logs/build_failure_summary.txt
