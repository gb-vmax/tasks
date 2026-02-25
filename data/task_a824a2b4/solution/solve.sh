#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/.dashboard_tune
printf 'DASHBOARD_TITLE=Staging Observability\nDEBUG_MODE=true\nLOG_LEVEL=info\nDATASOURCE_URL=https://logs-staging.example.com/query\nREFRESH_INTERVAL=30\n' > /home/user/.dashboard_tune/dashboard.env
export SESSION_OWNER="alice.smith" SESSION_ID="stag-20230501-001"
awk -F= 'NR==1{print "DASHBOARD_TITLE="$2} NR==2{print "DEBUG_MODE="$2} NR==3{print "LOG_LEVEL="$2} NR==4{print "DATASOURCE_URL="$2} NR==5{print "REFRESH_INTERVAL="$2}' /home/user/.dashboard_tune/dashboard.env > /home/user/.dashboard_tune/settings_merged.log && printf "SESSION_OWNER=%s\nSESSION_ID=%s\n" "$SESSION_OWNER" "$SESSION_ID" >> /home/user/.dashboard_tune/settings_merged.log
cat /home/user/.dashboard_tune/dashboard.env && echo "---" && cat /home/user/.dashboard_tune/settings_merged.log && echo "---" && printenv | grep -E '^SESSION_OWNER=|^SESSION_ID='
