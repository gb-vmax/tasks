FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the logs directory
mkdir -p /home/user/logs

# Create the auth.log file with the expected content
cat > /home/user/logs/auth.log << 'EOF'
Mar 15 09:01:12 webserver sshd[10001]: Accepted password for deploy from 10.0.0.1 port 22 ssh2
Mar 15 09:03:44 webserver sshd[10002]: Failed password for alice from 192.168.1.10 port 54321 ssh2
Mar 15 09:05:21 webserver sshd[10003]: Failed password for invalid user bob from 10.0.0.5 port 43210 ssh2
Mar 15 09:07:33 webserver sshd[10004]: Failed password for alice from 192.168.1.10 port 54400 ssh2
Mar 15 09:08:55 webserver sshd[10005]: Failed password for root from 203.0.113.5 port 12345 ssh2
Mar 15 09:10:02 webserver sshd[10006]: Failed password for root from 203.0.113.5 port 12346 ssh2
Mar 15 09:11:18 webserver sshd[10007]: Failed password for alice from 192.168.1.10 port 54500 ssh2
Mar 15 09:13:45 webserver sshd[10008]: Accepted password for alice from 192.168.1.10 port 54600 ssh2
Mar 15 09:15:00 webserver sshd[10009]: Failed password for invalid user admin from 198.51.100.2 port 9922 ssh2
Mar 15 09:16:12 webserver sshd[10010]: Failed password for root from 203.0.113.5 port 12347 ssh2
Mar 15 09:18:30 webserver sshd[10011]: Failed password for invalid user bob from 10.0.0.5 port 43300 ssh2
Mar 15 09:20:05 webserver sshd[10012]: Failed password for root from 203.0.113.5 port 12348 ssh2
Mar 15 09:22:44 webserver sshd[10013]: Failed password for invalid user admin from 198.51.100.2 port 9923 ssh2
Mar 15 09:25:10 webserver sshd[10014]: Accepted password for deploy from 10.0.0.1 port 22 ssh2
Mar 15 09:27:33 webserver sshd[10015]: Failed password for carol from 172.16.0.5 port 11111 ssh2
EOF

# Do NOT create the reports directory - the test asserts it does not exist yet

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
