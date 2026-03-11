#!/bin/bash
set -e
cd /home/user

find /home/user/deployments/ -type f -name "*.conf" | head -20
grep -rl "sk-OLDKEY-v1-abc123def456" /home/user/deployments/ --include="*.conf"
grep -rl "sk-OLDKEY-v1-abc123def456" /home/user/deployments/ --include="*.conf" | sort > /home/user/rotation_audit.log
sed -i 's/sk-OLDKEY-v1-abc123def456/sk-NEWKEY-v2-xyz789uvw012/g' /home/user/deployments/db/primary.conf /home/user/deployments/app/service.conf /home/user/deployments/gateway/proxy.conf
cat /home/user/rotation_audit.log
grep -rl "sk-OLDKEY-v1-abc123def456" /home/user/deployments/ --include="*.conf"
grep -rl "sk-NEWKEY-v2-xyz789uvw012" /home/user/deployments/ --include="*.conf"
