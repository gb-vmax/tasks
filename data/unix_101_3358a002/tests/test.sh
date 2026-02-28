#!/bin/bash
set -e
out=$(getfacl -R -n /home/user/project/)
echo "$out" | grep -q 'user:1001:rw-'
echo "$out" | grep -q 'group:1002:r--'
echo "$out" | grep -q '# file: /home/user/project/code.py'
echo "$out" | grep -q '# file: /home/user/project/subdir/note.txt'
echo 1 > /logs/verifier/reward.txt
