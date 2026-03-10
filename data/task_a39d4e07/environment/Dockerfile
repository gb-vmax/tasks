FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the finops directory
mkdir -p /home/user/finops

# Create the initial .env file with the expected content
cat > /home/user/finops/.env << 'EOF'
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
COST_ALERT_THRESHOLD_USD=500
MONTHLY_BUDGET_USD=3000
ALERT_EMAIL=old-analyst@company.com
UNUSED_LEGACY_KEY=abc123deprecated
ENABLE_COST_EXPLORER=true
OLD_REGION_OVERRIDE=eu-west-1
REPORT_INTERVAL_DAYS=7
DEBUG_VERBOSE=true
COST_ALLOCATION_TAG=CostCenter
BILLING_API_TOKEN=tok_live_9xKp2mNqRsTuVwXy
EOF

# Do NOT create .env.production — that's the agent's job

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
