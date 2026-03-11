FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the observer group
groupadd -f observer

# Create the dashboards directory
mkdir -p /home/user/dashboards

# Create the dashboard config files with specified content and 644 permissions
cat > /home/user/dashboards/grafana_main.json << 'EOF'
{"title": "Main Dashboard", "panels": []}
EOF

cat > /home/user/dashboards/alerts_config.json << 'EOF'
{"alerts": [], "routes": []}
EOF

printf '[datasource]\nhost=localhost\nport=5432' > /home/user/dashboards/datasources.cfg

# Set permissions to 644 (initial state before agent makes changes)
chmod 644 /home/user/dashboards/grafana_main.json
chmod 644 /home/user/dashboards/alerts_config.json
chmod 644 /home/user/dashboards/datasources.cfg

# Set ownership to user:user (initial state)
chown -R user:user /home/user/dashboards
ENDSETUP

WORKDIR /home/user
