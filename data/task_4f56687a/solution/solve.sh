#!/bin/bash
set -e
cd /home/user

mkdir -p workspace_links
ln -s /home/user/project_alpha/main.py workspace_links/alpha_main.py
ln -s /home/user/project_alpha/scripts/helper.sh workspace_links/alpha_helper.sh

cat > workspace_links/symlink_creation.log << 'EOF'
alpha_main.py -> /home/user/project_alpha/main.py
alpha_helper.sh -> /home/user/project_alpha/scripts/helper.sh
EOF
