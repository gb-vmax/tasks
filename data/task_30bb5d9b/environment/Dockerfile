FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the monitoring directory
mkdir -p /home/user/monitoring

# Create the metrics CSV file
cat > /home/user/monitoring/metrics.csv << 'EOF'
server,metric,value
webserver01,cpu_usage,45.0
webserver01,cpu_usage,60.0
webserver01,cpu_usage,75.0
webserver01,mem_usage,70.0
webserver01,mem_usage,82.0
webserver01,mem_usage,91.0
webserver01,mem_usage,65.0
dbserver01,cpu_usage,30.0
dbserver01,cpu_usage,55.0
dbserver01,cpu_usage,50.0
dbserver01,disk_io,120.0
dbserver01,disk_io,200.0
dbserver01,disk_io,160.0
dbserver01,disk_io,180.0
dbserver01,disk_io,140.0
EOF

# Do NOT create alert_thresholds.cfg — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
