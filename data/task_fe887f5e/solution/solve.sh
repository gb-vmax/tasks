#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/deployments/v2_1_release/
find /home/user/webapp_updates/ -maxdepth 1 -type f -exec mv {} /home/user/deployments/v2_1_release/ \;
(echo "Moved files:" && find /home/user/deployments/v2_1_release/ -maxdepth 1 -type f -printf "%f\n" | sort) > /home/user/update_log.txt
cat /home/user/update_log.txt
