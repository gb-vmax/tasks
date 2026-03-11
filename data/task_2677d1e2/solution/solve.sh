#!/bin/bash
set -e
cd /home/user

cat /home/user/migration/services.log
grep '\[FAILED\]' /home/user/migration/services.log | sed 's/.*\[FAILED\] \(.*\) ::.*/\1/' | sort > /home/user/migration/failed_services.txt
cat /home/user/migration/failed_services.txt
