#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/alerts/
printf "THRESHOLD=85\nNOTIFY_EMAIL=on\nLOGFILE=/home/user/alerts/alert.log\nENABLED=true\n" > /home/user/alerts/service_alerts.conf
touch /home/user/alerts/alert.log && chmod 600 /home/user/alerts/alert.log
echo "[2024-06-11 12:00:00] ALERT: THRESHOLD exceeded (value: 92)" > /home/user/alerts/alert.log
