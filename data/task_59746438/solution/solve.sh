#!/bin/bash
set -e
cd /home/user

id -u analyst01 2>/dev/null || sudo useradd analyst01
getent group analytics || sudo groupadd analytics
sudo mkdir -p /home/user/team_projects/analytics_data && sudo chown analyst01:analytics /home/user/team_projects/analytics_data
mkdir -p /home/user/team_projects/analytics_data && chown analyst01:analytics /home/user/team_projects/analytics_data
chmod 770 /home/user/team_projects/analytics_data
ls -ld /home/user/team_projects/analytics_data | awk '{print "/home/user/team_projects/analytics_data", $3, $4, $1}' > /home/user/analytics_permission_report.txt
cat /home/user/analytics_permission_report.txt
