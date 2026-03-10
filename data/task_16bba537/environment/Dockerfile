FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/fw_deny.log << 'EOF'
2024-11-01T08:12:03 DENY src=192.168.1.45 dst=10.0.0.1 port=443 proto=TCP
2024-11-01T08:12:11 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP
2024-11-01T08:13:00 DENY src=192.168.1.45 dst=10.0.0.1 port=80 proto=TCP
2024-11-01T08:13:45 DENY src=172.16.8.99 dst=10.0.0.2 port=8080 proto=TCP
2024-11-01T08:14:02 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP
2024-11-01T08:14:30 DENY src=192.168.1.45 dst=10.0.0.1 port=443 proto=TCP
2024-11-01T08:15:01 DENY src=10.10.5.2 dst=10.0.0.3 port=3389 proto=TCP
2024-11-01T08:15:22 DENY src=172.16.8.99 dst=10.0.0.2 port=443 proto=TCP
2024-11-01T08:16:10 DENY src=192.168.1.45 dst=10.0.0.1 port=8443 proto=TCP
2024-11-01T08:16:55 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP
2024-11-01T08:17:03 DENY src=192.168.1.45 dst=10.0.0.2 port=80 proto=TCP
2024-11-01T08:17:44 DENY src=172.16.8.99 dst=10.0.0.1 port=53 proto=UDP
2024-11-01T08:18:05 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP
2024-11-01T08:18:50 DENY src=192.168.1.45 dst=10.0.0.3 port=443 proto=TCP
2024-11-01T08:19:12 DENY src=172.16.8.99 dst=10.0.0.1 port=80 proto=TCP
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
