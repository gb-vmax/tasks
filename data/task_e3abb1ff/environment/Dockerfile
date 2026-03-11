FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/iot

cat > /home/user/iot/devices.csv << 'EOF'
device_id,location,firmware_version,ip_address,status,last_seen
sensor-001,factory-floor,1.9.4,10.0.0.11,active,2024-10-30
sensor-002,loading-dock,2.0.1,10.0.0.22,inactive,2024-10-28
sensor-003,rooftop,2.1.0,10.0.0.33,active,2024-11-01
sensor-004,warehouse-b,2.1.0,10.0.0.44,active,2024-11-01
sensor-005,parking-lot,1.8.7,10.0.0.55,maintenance,2024-10-15
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
