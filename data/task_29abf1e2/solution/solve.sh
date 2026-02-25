#!/bin/bash
set -e
cd /home/user

awk -F'CPU: |%,' '{ cpu=($2+0); if (cpu>50) print $0 }' /home/user/profile.log | tee /home/user/high_cpu_processes.txt | wc -l
cat /home/user/high_cpu_processes.txt
