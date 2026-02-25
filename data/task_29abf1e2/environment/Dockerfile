FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
cat > /home/user/profile.log <<EOF
PID: 4521, CPU: 23.1%, MEM: 125MB, CMD: myapp
PID: 4522, CPU: 88.6%, MEM: 300MB, CMD: data-collector
PID: 4523, CPU: 11.8%, MEM: 89MB, CMD: helper
PID: 4524, CPU: 67.2%, MEM: 200MB, CMD: analytics
PID: 4525, CPU: 50.0%, MEM: 230MB, CMD: renderer
PID: 4526, CPU: 99.1%, MEM: 100MB, CMD: cruncher
PID: 4527, CPU: 44.5%, MEM: 189MB, CMD: updater
EOF

# Do NOT create /home/user/high_cpu_processes.txt

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
