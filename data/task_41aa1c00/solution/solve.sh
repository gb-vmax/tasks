#!/bin/bash
set -e
cd /home/user

grep -n 'refresh_interval' /home/user/observability/dashboard_config/dashboard_metrics.yaml
sed -i '5i# Increased refresh interval from 30s to 60s on request' /home/user/observability/dashboard_config/dashboard_metrics.yaml && sed -i '6s/30s/60s/' /home/user/observability/dashboard_config/dashboard_metrics.yaml
echo "[`date -u '+%Y-%m-%d %H:%M:%S'`] user: Refreshed dashboard_metrics.yaml interval to 60s" >> /home/user/observability/dashboard_config/audit.log
tail -10 /home/user/observability/dashboard_config/dashboard_metrics.yaml && tail -2 /home/user/observability/dashboard_config/audit.log
