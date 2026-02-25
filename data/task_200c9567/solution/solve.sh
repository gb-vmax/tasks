#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/deployments/analytics-app && chown user:user /home/user/deployments/analytics-app
export TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)" && \
ENV=/home/user/deployments/analytics-app/.env && \
( grep -v -E '^(APP_VERSION|DATABASE_URL|ENABLE_CACHE|LOG_LEVEL|DEPLOY_TIMESTAMP)=' "$ENV" 2>/dev/null || true ; \
echo "APP_VERSION=3.8.2" ; \
echo "DATABASE_URL=postgresql://analytics:Password123@db.internal:5432/analyticsdb" ; \
echo "ENABLE_CACHE=true" ; \
echo "LOG_LEVEL=info" ; \
echo "DEPLOY_TIMESTAMP=$TS" ) > "$ENV"
TS=$(grep '^DEPLOY_TIMESTAMP=' /home/user/deployments/analytics-app/.env | cut -d= -f2-) && \
echo "[DEPLOYED] $TS - version 3.8.2 deployed by user" > /home/user/deployments/analytics-app/deploy.log
chmod 660 /home/user/deployments/analytics-app/.env /home/user/deployments/analytics-app/deploy.log && chown user:user /home/user/deployments/analytics-app/.env /home/user/deployments/analytics-app/deploy.log
cat /home/user/deployments/analytics-app/.env && echo /home/user/deployments/analytics-app/deploy.log && cat /home/user/deployments/analytics-app/deploy.log
