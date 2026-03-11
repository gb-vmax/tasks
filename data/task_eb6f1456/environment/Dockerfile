FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the audit_logs directory
mkdir -p /home/user/audit_logs

# Create access.log
cat > /home/user/audit_logs/access.log << 'EOF'
192.168.1.10 - - [01/Jul/2024 08:12:03] "GET /dashboard HTTP/1.1" 200 4523
192.168.1.22 - - [01/Jul/2024 08:14:55] "POST /login HTTP/1.1" 200 312
192.168.1.45 - - [01/Jul/2024 08:19:30] "GET /reports HTTP/1.1" 403 89
EOF

# Create error.log
cat > /home/user/audit_logs/error.log << 'EOF'
[01/Jul/2024 08:19:30] ERROR: Access denied for user 'jsmith' on /reports
[02/Jul/2024 11:43:01] ERROR: Database connection timeout after 30s
[03/Jul/2024 09:05:17] ERROR: Invalid session token from 10.0.0.8
EOF

# Create auth.log
cat > /home/user/audit_logs/auth.log << 'EOF'
Jul 01 08:14:55 appserver sshd[1042]: Accepted password for deploy from 192.168.1.22 port 54312 ssh2
Jul 02 14:22:10 appserver sshd[1198]: Failed password for root from 10.0.0.99 port 41200 ssh2
Jul 03 09:00:01 appserver sudo: jsmith : TTY=pts/0 ; PWD=/home/jsmith ; USER=root ; COMMAND=/bin/cat /etc/shadow
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
