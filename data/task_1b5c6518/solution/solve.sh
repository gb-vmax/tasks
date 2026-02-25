#!/bin/bash
set -e
cd /home/user

cat > release_configs/app.yaml << 'EOF'
release: 2.1.0
changelog:
  - Added feature X
  - Fixed bug Y
config:
  debug: false
  port: 8080
EOF

cat > release_configs/database.toml << 'EOF'
[connection]
host = "db.internal"
port = 5432
max_active = 40
EOF

printf '%s\n' \
  'Updated app.yaml release version to 2.1.0' \
  'Added changelog to app.yaml' \
  'Set database.toml connection.max_active to 40' \
  > release_configs/config_update.log
