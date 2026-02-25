#!/bin/bash
set -euo pipefail

# Append deploy step to build.yml
cat >> /home/user/workflows/build.yml << 'EOF'
  - name: deploy
    run: ./deploy.sh
EOF

# Create edit.log with exact content (no trailing newline)
printf "Step 'deploy' added to build.yml" > /home/user/workflows/edit.log
