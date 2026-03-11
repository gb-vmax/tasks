FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/monitoring

cat > /home/user/monitoring/cpu_mem.csv << 'EOF'
timestamp,cpu_percent,mem_used_mb,mem_total_mb
2024-05-10 09:00,45.2,3200,8192
2024-05-10 09:01,78.5,3400,8192
2024-05-10 09:02,91.3,3600,8192
2024-05-10 09:03,62.1,3100,8192
2024-05-10 09:04,55.0,3250,8192
2024-05-10 09:05,83.7,4000,8192
2024-05-10 09:06,47.9,3150,8192
2024-05-10 09:07,70.4,3300,8192
2024-05-10 09:08,88.6,3900,8192
2024-05-10 09:09,66.2,3450,8192
EOF

cat > /home/user/monitoring/disk_usage.txt << 'EOF'
/ 42 100
/boot 0.4 1
/home 310 400
/var 75 80
EOF

cat > /home/user/monitoring/processes.log << 'EOF'
[2024-05-10 09:00] nginx 1021 running 1.2
[2024-05-10 09:00] postgres 1055 sleeping 0.4
[2024-05-10 09:00] python3 2310 running 45.7
[2024-05-10 09:01] nginx 1021 running 1.5
[2024-05-10 09:01] python3 2310 running 88.3
[2024-05-10 09:01] defunct 3001 zombie 0.0
[2024-05-10 09:02] nginx 1021 sleeping 0.8
[2024-05-10 09:02] postgres 1055 sleeping 0.3
[2024-05-10 09:02] python3 2310 running 91.1
[2024-05-10 09:03] defunct 3001 zombie 0.0
[2024-05-10 09:03] nginx 1021 running 2.1
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
