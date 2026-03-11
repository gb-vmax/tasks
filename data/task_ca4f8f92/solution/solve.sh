#!/bin/bash
set -e
cd /home/user

cat /home/user/finops/cost_alerts.cfg
sed -i 's/^monthly_budget_usd=.*/monthly_budget_usd=12500/' /home/user/finops/cost_alerts.cfg && sed -i 's/^alert_threshold_pct=.*/alert_threshold_pct=80/' /home/user/finops/cost_alerts.cfg && sed -i 's/^owner_email=.*/owner_email=finops-team@company.com/' /home/user/finops/cost_alerts.cfg
cat /home/user/finops/cost_alerts.cfg
printf 'BUDGET: $12500 | ALERT AT: 80%% | CONTACT: finops-team@company.com' > /home/user/finops/budget_summary.txt
cat /home/user/finops/budget_summary.txt
