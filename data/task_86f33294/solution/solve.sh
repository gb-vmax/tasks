#!/bin/bash
set -e
cd /home/user

ls -la /home/user/deployments/
ln -sfn /home/user/deployments/releases/v2.4.0 /home/user/deployments/current
ln -sn /home/user/deployments/releases/v2.3.1 /home/user/deployments/previous
printf "current -> %s\nprevious -> %s\n" "$(readlink /home/user/deployments/current)" "$(readlink /home/user/deployments/previous)" > /home/user/deployments/deploy_log.txt
readlink /home/user/deployments/current && readlink /home/user/deployments/previous && echo "---" && cat /home/user/deployments/deploy_log.txt
