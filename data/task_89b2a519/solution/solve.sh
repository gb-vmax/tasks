#!/bin/bash
set -e
cd /home/user

yq -i '.settings.debug = false' /home/user/project/config/app_config.yaml
sed -i '/^[[:space:]]*debug:[[:space:]]*true[[:space:]]*$/s/true/false/' /home/user/project/config/app_config.yaml
cat /home/user/project/config/app_config.yaml
sed -i '/^[[:space:]]*- logging[[:space:]]*$/a\  - notification' /home/user/project/config/app_config.yaml
cat /home/user/project/config/env_config.toml
awk 'BEGIN{in_server=0} /^\[server\]/ {in_server=1} /^\[.*\]/ && $0!~/^\[server\]/ {in_server=0} {if(in_server && /^PORT[[:space:]]*=/){sub(/8080/,9090)}}{print}' /home/user/project/config/env_config.toml > /home/user/project/config/env_config.tmp && mv /home/user/project/config/env_config.tmp /home/user/project/config/env_config.toml
sed -i '/^\[database\]/,/^\[/ {/^url[[:space:]]*=/a timeout = 30}' /home/user/project/config/env_config.toml
sed -i '/^url *=/a timeout = 30' /home/user/project/config/env_config.toml
cat > /home/user/project/incident_report.log << 'EOF'
app_config.yaml:
- Set settings.debug to false
- Added 'notification' to services list

env_config.toml:
- Set server.PORT to 9090
- Added database.timeout = 30
EOF
