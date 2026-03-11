FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the finops directory
mkdir -p /home/user/finops

# Create the initial cost_alerts.cfg file with the expected content
cat > /home/user/finops/cost_alerts.cfg << 'EOF'
environment=production
cloud_provider=aws
monthly_budget_usd=9000
alert_threshold_pct=75
currency=USD
owner_email=analyst@company.com
notify_slack=true
slack_channel=#cloud-costs
EOF

# Do NOT create budget_summary.txt - the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
