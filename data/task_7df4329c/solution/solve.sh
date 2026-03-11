#!/bin/bash
set -e
cd /home/user

ls /home/user/audit_logs/
mkdir -p /home/user/submissions/
tar -czvf /home/user/submissions/audit_march_2024.tar.gz -C /home/user/audit_logs/ access_2024-03-01.log access_2024-03-08.log access_2024-03-15.log access_2024-03-22.log access_2024-03-29.log
tar -tzvf /home/user/submissions/audit_march_2024.tar.gz > /home/user/submissions/audit_march_2024_manifest.txt
cat /home/user/submissions/audit_march_2024_manifest.txt
echo "=== Archive contents ===" && tar -tzvf /home/user/submissions/audit_march_2024.tar.gz && echo "" && echo "=== Manifest line count ===" && wc -l /home/user/submissions/audit_march_2024_manifest.txt && echo "" && echo "=== Submissions directory ===" && ls -lh /home/user/submissions/
