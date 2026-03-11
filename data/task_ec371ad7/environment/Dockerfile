FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create project directory
mkdir -p /home/user/project

# Create the deploy.ini file with the expected content
cat > /home/user/project/deploy.ini << 'EOF'
[development]
host = localhost
port = 5000
debug = true
db = dev_db

[staging]
host = staging.myapp.io
port = 8080
debug = false
db = staging_db

[production]
host = prod.myapp.io
port = 443
debug = false
db = prod_db
EOF

# Do NOT create config_summary.txt — the agent will create it
# Do NOT append "; summary generated" — the agent will do that

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
