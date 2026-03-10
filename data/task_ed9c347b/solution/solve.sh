#!/bin/bash
set -e
cd /home/user

cat /home/user/project/build.log
grep -E '^src/[^:]+\.c:[0-9]+:[0-9]+: warning: ' /home/user/project/build.log > /home/user/project/warnings.txt
cat /home/user/project/warnings.txt
