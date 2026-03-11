#!/bin/bash
set -e
cd /home/user

cat /home/user/builds/nightly.log
grep '\[FAILED\]' /home/user/builds/nightly.log | sed 's/.*artifact=\([^ ]*\) .*/\1/' > /home/user/builds/failed_artifacts.txt
cat /home/user/builds/failed_artifacts.txt
