FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/audit

cat > /home/user/audit/access_log.tsv << 'EOF'
timestamp	username	server_id	ip_address	access_level	session_duration_mins
2024-06-01T08:12:00Z	jsmith	SRV-01	192.168.1.10	admin	45
2024-06-01T08:45:00Z	ajones	SRV-02	192.168.1.22	read-only	12
2024-06-01T09:03:00Z	bwilliams	SRV-01	10.0.0.5	read-write	30
2024-06-01T09:17:00Z	jsmith	SRV-03	192.168.1.10	admin	60
2024-06-01T10:02:00Z	mchen	SRV-02	10.0.0.8	read-only	8
2024-06-01T10:45:00Z	rdavis	SRV-01	192.168.2.15	read-write	22
2024-06-01T11:30:00Z	ajones	SRV-03	192.168.1.22	admin	90
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
