FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create monitoring directory
mkdir -p /home/user/monitoring

# Create the check_alerts.sh script (not executable, mode 644)
cat > /home/user/monitoring/check_alerts.sh << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$SCRIPT_DIR/cpu_usage.log"

while IFS=' ' read -r hostname timestamp cpu; do
    if awk -v val="$cpu" 'BEGIN { exit !(val > 80.0) }'; then
        echo "ALERT: $hostname exceeded threshold at $timestamp (CPU: ${cpu}%)"
    fi
done < "$LOG_FILE"
EOF

# Set permissions to 644 (not executable)
chmod 644 /home/user/monitoring/check_alerts.sh

# Create the cpu_usage.log file
cat > /home/user/monitoring/cpu_usage.log << 'EOF'
webserver01 2024-03-15T08:00:00 45.2
webserver02 2024-03-15T08:00:00 91.7
webserver01 2024-03-15T08:05:00 78.4
webserver03 2024-03-15T08:05:00 83.1
webserver02 2024-03-15T08:05:00 55.0
webserver01 2024-03-15T08:10:00 99.3
webserver03 2024-03-15T08:10:00 80.0
webserver02 2024-03-15T08:10:00 62.8
webserver01 2024-03-15T08:15:00 81.5
webserver03 2024-03-15T08:15:00 77.9
EOF

# Do NOT create alerts_output.txt — the agent must create it

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
