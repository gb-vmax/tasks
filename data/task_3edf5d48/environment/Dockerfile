FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the incident directory
mkdir -p /home/user/incident

# Create the analyze_log.py script with LOG_THRESHOLD on line 10
cat > /home/user/incident/analyze_log.py << 'EOF'
import os
import sys

# Legacy log analysis script v1.3
# Author: ops-team
# Last modified: 2024-01-10
# Usage: set LOG_THRESHOLD env var before running

log_path = "/home/user/incident/server.log"
threshold = int(os.environ["LOG_THRESHOLD"])

flagged = []
with open(log_path) as f:
    for line in f:
        line = line.strip()
        if line.startswith("[ERROR]"):
            flagged.append(line)

above = [e for e in flagged if True]
if len(above) > threshold:
    print(f"Lines above threshold: {len(above)}")
    print("Flagged entries:")
    for entry in above:
        print(f"  {entry}")
else:
    print("No issues detected.")
EOF

# Create the server.log file with exactly 4 [ERROR] lines
cat > /home/user/incident/server.log << 'EOF'
[INFO] server started on port 8080
[INFO] loaded config from /etc/app/config.yaml
[ERROR] disk quota exceeded
[INFO] retrying connection to database
[ERROR] connection timeout
[WARNING] memory usage at 87%
[ERROR] failed to write to socket
[INFO] health check passed
[ERROR] null pointer in handler
[INFO] scheduled backup completed
EOF

# Set correct ownership
chown -R user:user /home/user
EOF
ENDSETUP

WORKDIR /home/user
