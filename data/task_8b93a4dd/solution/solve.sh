#!/bin/bash
set -e
cd /home/user

head -20 /home/user/logs/service.log
grep '^[ERROR]' /home/user/logs/service.log
grep -F '[ERROR]' /home/user/logs/service.log
grep -F '[ERROR]' /home/user/logs/service.log > /home/user/logs/errors_only.log
grep -cF '[ERROR]' /home/user/logs/service.log > /home/user/logs/error_count.txt
cat /home/user/logs/error_count.txt && echo "---" && cat /home/user/logs/errors_only.log
