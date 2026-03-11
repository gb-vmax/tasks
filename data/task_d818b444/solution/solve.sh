#!/bin/bash
set -e
cd /home/user

cat /home/user/etl/pipeline.log
grep -E '^\S+ \S+ \| ERROR \| \[(TRANSFORM|LOAD)\] \|' /home/user/etl/pipeline.log > /home/user/etl/errors.log
wc -l < /home/user/etl/errors.log | tr -d ' ' > /home/user/etl/error_count.txt
cat /home/user/etl/errors.log && echo "---" && cat /home/user/etl/error_count.txt
