FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/project/config

cat > /home/user/project/config/app_config.yaml <<'EOF'
settings:
  debug: true
  version: "1.2.3"
services:
  - web
  - auth
  - logging
EOF

cat > /home/user/project/config/env_config.toml <<'EOF'
[server]
HOST = "0.0.0.0"
PORT = 8080

[database]
url = "postgres://user:pass@localhost/db"
EOF

# Do NOT create /home/user/project/incident_report.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
