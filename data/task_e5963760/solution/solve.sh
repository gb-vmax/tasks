#!/bin/bash
set -e
cd /home/user

grep '^ERROR:' /home/user/builds/build_output.log | awk '!seen[$0]++' > /home/user/builds/build_errors_summary.txt
cat /home/user/builds/build_errors_summary.txt
