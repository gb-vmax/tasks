FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the monitoring/alerts directory structure
mkdir -p /home/user/monitoring/alerts

# Create the alert config files
echo -e "alert: HighCPU\nthreshold: 90" > /home/user/monitoring/alerts/cpu_high.yml
echo -e "alert: DiskFull\nthreshold: 85" > /home/user/monitoring/alerts/disk_full.yml
echo -e "alert: LowMemory\nthreshold: 10" > /home/user/monitoring/alerts/memory_low.yml

# Do NOT create /home/user/backups/ — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
