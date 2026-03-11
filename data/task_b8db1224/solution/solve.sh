#!/bin/bash
set -e
cd /home/user

cat /home/user/mlops/experiments.tsv
awk -F'\t' '$3 == "COMPLETED" { 
    acc = sprintf("%.1f%%", $4 * 100);
    split($5, a, "/");
    ckpt = a[length(a)];
    sub(/\.pt$/, "", ckpt);
    print $1 " | " $2 " | " acc " | " ckpt
}' /home/user/mlops/experiments.tsv > /home/user/mlops/artifact_report.txt
cat /home/user/mlops/artifact_report.txt
