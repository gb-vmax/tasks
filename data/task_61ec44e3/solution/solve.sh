#!/bin/bash
set -e
cd /home/user

cat /home/user/monitoring/check_alerts.sh
chmod +x /home/user/monitoring/check_alerts.sh && /home/user/monitoring/check_alerts.sh > /home/user/monitoring/alerts_output.txt
cat /home/user/monitoring/alerts_output.txt
