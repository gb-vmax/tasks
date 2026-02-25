#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/releases/deployments && tail -n +2 /home/user/releases/service_list.csv | while IFS=, read -r service_name current_version next_version maintainer; do printf "service:\n  name: %s\n  deploy_version: %s\n  maintainer: %s\n  changelog: |\n    Upgraded from %s to %s in this release.\n" "$service_name" "$next_version" "$maintainer" "$current_version" "$next_version" > "/home/user/releases/deployments/${service_name}-deploy.yaml"; done && ls /home/user/releases/deployments | sort > /home/user/releases/deployment_manifest.log
cat /home/user/releases/deployment_manifest.log
cat /home/user/releases/deployments/auth-service-deploy.yaml
