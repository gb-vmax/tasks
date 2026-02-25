#!/bin/bash
set -e
cd /home/user

grep -E '\[.*\] (ERROR|WARNING) - ' /home/user/sample_data.log > /home/user/filtered_errors_warnings.log
cat /home/user/filtered_errors_warnings.log
