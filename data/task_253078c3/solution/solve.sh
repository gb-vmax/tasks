#!/bin/bash
set -e
cd /home/user

awk '/ERROR/ {sub(/^.*ERROR /,""); print}' /home/user/kube-manifests/logs/deploy_onboarding.log | sort | uniq -c | sort -k2 | awk '{count=$1; $1=""; sub(/^ /,""); print $0 ": " count}' > /home/user/kube-manifests/reports/error_summary.log
cat /home/user/kube-manifests/reports/error_summary.log
