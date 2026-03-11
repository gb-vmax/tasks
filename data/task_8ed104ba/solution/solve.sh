#!/bin/bash
set -e
cd /home/user

id user 2>/dev/null && echo "user exists" || echo "user does not exist"
sudo groupadd monitors
sudo useradd --no-create-home --shell /usr/sbin/nologin -G monitors alertagent
sudo useradd --no-create-home --shell /usr/sbin/nologin -G monitors logreader
mkdir -p /home/user/alertsys/configs /home/user/alertsys/logs /home/user/alertsys/reports
sudo chown alertagent:monitors /home/user/alertsys/configs && sudo chmod 750 /home/user/alertsys/configs
sudo chown logreader:monitors /home/user/alertsys/logs && sudo chmod 770 /home/user/alertsys/logs
sudo chown user:monitors /home/user/alertsys/reports && sudo chmod 775 /home/user/alertsys/reports
sudo tee /home/user/alertsys/configs/threshold.conf > /dev/null << 'EOF'
cpu_threshold=85
mem_threshold=90
disk_threshold=80
EOF
sudo chown alertagent:monitors /home/user/alertsys/configs/threshold.conf && sudo chmod 640 /home/user/alertsys/configs/threshold.conf
sudo tee /home/user/alertsys/logs/alert.log > /dev/null << 'EOF'
2024-06-01T08:00:00Z INFO monitoring started
2024-06-01T08:15:22Z WARN cpu usage at 87%
2024-06-01T08:16:01Z ALERT disk usage at 83%
EOF
sudo chown logreader:monitors /home/user/alertsys/logs/alert.log && sudo chmod 660 /home/user/alertsys/logs/alert.log
tee /home/user/alertsys/reports/daily_summary.txt > /dev/null << 'EOF'
Date: 2024-06-01
Alerts triggered: 2
Status: review required
EOF
sudo chown user:monitors /home/user/alertsys/reports/daily_summary.txt && sudo chmod 664 /home/user/alertsys/reports/daily_summary.txt
tee /home/user/alertsys/audit_report.txt > /dev/null << 'EOF'
=== ALERTSYS PERMISSION AUDIT ===

[DIRECTORIES]
path=/home/user/alertsys/configs owner=alertagent group=monitors perms=750
path=/home/user/alertsys/logs owner=logreader group=monitors perms=770
path=/home/user/alertsys/reports owner=user group=monitors perms=775

[FILES]
path=/home/user/alertsys/configs/threshold.conf owner=alertagent group=monitors perms=640
path=/home/user/alertsys/logs/alert.log owner=logreader group=monitors perms=660
path=/home/user/alertsys/reports/daily_summary.txt owner=user group=monitors perms=664

[SUMMARY]
total_directories=3
total_files=3
group_verified=monitors
EOF
sudo chown user:user /home/user/alertsys/audit_report.txt && sudo chmod 644 /home/user/alertsys/audit_report.txt
