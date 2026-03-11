FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/metrics

cat > /home/user/metrics/cpu_usage.log << 'EOF'
web01 2024-03-15T09:00:00 82.5
web02 2024-03-15T09:00:00 67.3
db01 2024-03-15T09:00:00 91.2
web01 2024-03-15T09:05:00 79.1
web02 2024-03-15T09:05:00 55.8
db01 2024-03-15T09:05:00 88.4
web01 2024-03-15T09:10:00 BADVAL
web02 2024-03-15T09:10:00 71.0
db01 2024-03-15T09:10:00 94.7
web01 2024-03-15T09:10:00 85.6
cache01 2024-03-15T09:00:00 43.2
cache01 2024-03-15T09:05:00 incomplete_line_no_cpu
cache01 2024-03-15T09:10:00 47.8
db01 2024-03-15T09:15:00 89.9
web02 2024-03-15T09:15:00 60.4
EOF

cat > /home/user/metrics/memory_usage.log << 'EOF'
web01 3072 8192
web02 5120 8192
# db01 is undergoing maintenance
db01 14000 16384
web01 4096 8192
cache01 1024 4096
# temporary comment
web02 6144 8192
db01 15000 16384
cache01 2048 4096
EOF

cat > /home/user/metrics/disk_usage.log << 'EOF'
/var/log 120 500
/home/user data 800 2000
/tmp 600 400
/data/postgres 1800 2000
/mnt/backup storage 3500 5000
/var/cache 90 200
/tmp 600 400
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
