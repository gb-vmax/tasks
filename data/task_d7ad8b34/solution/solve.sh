#!/bin/bash
set -e
cd /home/user

grep -E '^2024-06-1[0-6] [0-9]{2}:[0-9]{2}:[0-9]{2} \[(ERROR|WARN)\]' /home/user/appdata/app.log > /home/user/diagnostics/filtered_errors_warnings.log
cat /home/user/diagnostics/filtered_errors_warnings.log
