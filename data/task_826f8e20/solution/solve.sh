#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/user/my_python_project"

# Write settings.yaml
cat > "${PROJECT_DIR}/settings.yaml" << 'EOF'
database:
  host: localhost
  port: 5432
  user: admin
  password: secret123
EOF

# Write config.toml
cat > "${PROJECT_DIR}/config.toml" << 'EOF'
[project]
name = "my_python_project"
version = "1.0.0"
EOF

# Write config_update.log with exact format
cat > "${PROJECT_DIR}/config_update.log" << 'EOF'
=== settings.yaml ===
database:
  host: localhost
  port: 5432
  user: admin
  password: secret123
=== config.toml ===
[project]
name = "my_python_project"
version = "1.0.0"
EOF
