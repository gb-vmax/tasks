#!/bin/bash
set -e
cd /home/user

grep -E 'ERROR:[[:space:]]*[a-zA-Z0-9_-]+[[:space:]]+deploy failed' /home/user/migration/logs/deployments.log > /home/user/migration/logs/failed_services.log
cat /home/user/migration/logs/failed_services.log
