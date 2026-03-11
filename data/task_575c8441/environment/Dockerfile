FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the audit directory
mkdir -p /home/user/audit

# Create the access log TSV file with tab-separated values
cat > /home/user/audit/access_log.tsv << 'EOF'
timestamp	username	ip_address	system	action	status
2024-06-01T08:12:34Z	alice	10.0.1.5	payroll	LOGIN	SUCCESS
2024-06-01T08:45:00Z	bob	10.0.1.8	hr_portal	VIEW	SUCCESS
2024-06-01T09:03:11Z	alice	10.0.1.5	finance	EXPORT	DENIED
2024-06-01T09:17:55Z	charlie	10.0.2.1	payroll	LOGIN	SUCCESS
2024-06-01T10:01:22Z	bob	10.0.1.8	payroll	VIEW	SUCCESS
2024-06-01T10:34:09Z	diana	10.0.3.4	hr_portal	LOGIN	SUCCESS
2024-06-01T11:00:00Z	alice	10.0.1.5	hr_portal	DELETE	DENIED
2024-06-01T11:22:47Z	charlie	10.0.2.1	finance	VIEW	SUCCESS
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
