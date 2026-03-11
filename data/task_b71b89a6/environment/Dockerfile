FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/audit

cat > /home/user/audit/access_log.csv << 'EOF'
timestamp,username,action,source_ip,status
2024-01-15 08:23:41,alice,LOGIN,192.168.1.10,SUCCESS
2024-01-15 08:45:02,bob,LOGIN,10.0.0.5,FAILURE
2024-01-15 09:12:33,carol,LOGIN,192.168.1.22,FAILURE
2024-01-15 10:05:17,alice,LOGIN,192.168.1.10,FAILURE
2024-01-16 07:58:09,dave,LOGIN,10.0.0.8,SUCCESS
2024-01-16 11:30:55,bob,LOGIN,10.0.0.5,FAILURE
2024-01-17 14:02:44,carol,LOGIN,192.168.1.22,SUCCESS
2024-01-17 16:47:19,eve,LOGIN,172.16.0.3,FAILURE
2024-01-18 09:22:05,alice,LOGIN,192.168.1.10,FAILURE
2024-01-18 13:15:30,dave,LOGIN,10.0.0.8,FAILURE
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
