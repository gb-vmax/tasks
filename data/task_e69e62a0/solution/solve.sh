#!/bin/bash
set -e
cd /home/user

cat /home/user/profiling/cpu_profile.tsv
awk 'BEGIN{FS="\t"; OFS="\t"} {print $1, $5, $6, $3}' /home/user/profiling/cpu_profile.tsv > /home/user/profiling/summary.tsv
cat /home/user/profiling/summary.tsv
