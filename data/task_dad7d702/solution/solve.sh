#!/bin/bash
set -e
cd /home/user

ls /home/user/datasets/experiment_42/
mkdir -p /home/user/backups && tar -czf /home/user/backups/experiment_42_data.tar.gz -C /home/user/datasets/experiment_42 measurements_a.csv measurements_b.csv results_final.csv
tar -tzf /home/user/backups/experiment_42_data.tar.gz > /home/user/backups/experiment_42_manifest.txt
cat /home/user/backups/experiment_42_manifest.txt && echo "---" && ls /home/user/backups/
