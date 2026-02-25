FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/security

cat > /home/user/security/audit.log <<'EOF'
Jan 07 10:15:12 server1 sshd[1245]: Accepted password for bob from 10.0.0.5 port 4857 ssh2
Jan 07 10:16:33 server1 sshd[1247]: Failed password for alice from 10.0.0.7 port 5060 ssh2
Jan 07 10:18:02 server1 su[1250]: authentication failure; logname=bob uid=1000 euid=0 tty=pts/0 ruser=bob rhost=
Jan 07 10:20:59 server1 sshd[1262]: Connection closed by authenticating user alice 10.0.0.7 port 5088 [preauth]
Jan 07 10:21:12 server1 sshd[1270]: Failed password for invalid user admin from 10.0.0.12 port 5164 ssh2
Jan 07 10:22:50 server1 su[1275]: session opened for user root by bob(uid=1000)
Jan 07 10:23:18 server1 sshd[1279]: Failed password for root from 10.0.0.15 port 5210 ssh2
EOF

# Ensure audit.log is readable and writable by user
chown -R user:user /home/user
chmod 600 /home/user/security/audit.log
ENDSETUP

WORKDIR /home/user
