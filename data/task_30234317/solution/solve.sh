#!/bin/bash
set -e
cd /home/user

(echo "==== CRON JOBS FOR USER: alice ===="; if crontab -l -u alice 2>&1 | grep -q '^no crontab for'; then echo "No crontab for user alice"; else crontab -l -u alice | grep -v '^\s*#' | grep -v '^\s*$' | awk '{print "TIMING: " $1, $2, $3, $4, $5 "\nCOMMAND: " substr($0, index($0,$6))}'; fi) > /home/user/cron_audit_report.txt
(echo "==== CRON JOBS FOR USER: alice ===="; if [ -f /var/spool/cron/crontabs/alice ]; then grep -v '^\s*#' /var/spool/cron/crontabs/alice | grep -v '^\s*$' | awk '{print "TIMING: " $1, $2, $3, $4, $5 "\nCOMMAND: " substr($0, index($0,$6))}'; elif [ -f /var/spool/cron/alice ]; then grep -v '^\s*#' /var/spool/cron/alice | grep -v '^\s*$' | awk '{print "TIMING: " $1, $2, $3, $4, $5 "\nCOMMAND: " substr($0, index($0,$6))}'; else echo "No crontab for user alice"; fi) > /home/user/cron_audit_report.txt
(echo "==== CRON JOBS FOR USER: bob ===="; if [ -f /var/spool/cron/crontabs/bob ]; then grep -v '^\s*#' /var/spool/cron/crontabs/bob | grep -v '^\s*$' | awk '{print "TIMING: " $1, $2, $3, $4, $5 "\nCOMMAND: " substr($0, index($0,$6))}'; elif [ -f /var/spool/cron/bob ]; then grep -v '^\s*#' /var/spool/cron/bob | grep -v '^\s*$' | awk '{print "TIMING: " $1, $2, $3, $4, $5 "\nCOMMAND: " substr($0, index($0,$6))}'; else echo "No crontab for user bob"; fi) >> /home/user/cron_audit_report.txt
cat /home/user/cron_audit_report.txt
