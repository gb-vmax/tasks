#!/bin/bash
set -e
cd /home/user

find /home/user/project -type f | sort
find /home/user/project -not -path "*/logs_archive/*" -name "*.log" -print0 | xargs -0 mv -t /home/user/project/logs_archive/
find /home/user/project -not -path "*/logs_archive/*" -name "*.tmp" -print0 | xargs -0 rm -f
find /home/user/project -name "*.py" | sort > /home/user/project/py_manifest.txt
echo "=== logs_archive ===" && find /home/user/project/logs_archive -type f && echo "=== tmp files (should be empty) ===" && find /home/user/project -name "*.tmp" && echo "=== py_manifest.txt ===" && cat /home/user/project/py_manifest.txt
