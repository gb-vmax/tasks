#!/bin/bash
set -euo pipefail

# Create directory structure
mkdir -p /home/user/provisioning/configs
mkdir -p /home/user/provisioning/active

# Create config files (single line each)
printf 'WEB.CONF\n' > /home/user/provisioning/configs/web.conf
printf 'DB.CONF\n' > /home/user/provisioning/configs/db.conf
printf 'CACHE.CONF\n' > /home/user/provisioning/configs/cache.conf

# Create relative symlinks in active directory
cd /home/user/provisioning/active
ln -sf ../configs/web.conf web_active.conf
ln -sf ../configs/db.conf db_active.conf
ln -sf ../configs/cache.conf cache_active.conf

# Create symlink report
cat > /home/user/provisioning/symlink_report.txt << 'EOF'
web_active.conf,../configs/web.conf,WEB.CONF
db_active.conf,../configs/db.conf,DB.CONF
cache_active.conf,../configs/cache.conf,CACHE.CONF
EOF
