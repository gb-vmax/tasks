FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs

cat > /home/user/logs/auth_sample.log <<'EOF'
Jun 15 10:05:13 server1 sshd[531]: Accepted password for admin from 192.168.56.21 port 62420 ssh2
Jun 15 10:05:15 server1 chmod: mode of '/var/tmp/testfile.log' changed from 0644 to 0600
Jun 15 10:05:16 server1 su[540]: Successful su for root by admin
Jun 15 10:05:19 server1 chown: changing ownership of '/srv/www/html/index.html' from root to webuser
Jun 15 10:05:25 server1 sshd[531]: Session closed for admin
Jun 15 10:05:30 server1 passwd[550]: password for user 'bob' changed by admin
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
