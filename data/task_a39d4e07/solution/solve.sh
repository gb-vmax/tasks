#!/bin/bash
set -e
cd /home/user

cat /home/user/finops/.env
sed -i \
  -e 's/^COST_ALERT_THRESHOLD_USD=.*/COST_ALERT_THRESHOLD_USD=750/' \
  -e 's/^MONTHLY_BUDGET_USD=.*/MONTHLY_BUDGET_USD=5000/' \
  -e 's/^ALERT_EMAIL=.*/ALERT_EMAIL=finops-team@company.com/' \
  -e '/^UNUSED_LEGACY_KEY=/d' \
  -e '/^OLD_REGION_OVERRIDE=/d' \
  -e '/^DEBUG_VERBOSE=/d' \
  /home/user/finops/.env
cat /home/user/finops/.env
grep -E '^[A-Z]' /home/user/finops/.env | grep -vE '^[^=]*(KEY|SECRET|TOKEN)[^=]*=' > /home/user/finops/.env.production
cat /home/user/finops/.env.production
