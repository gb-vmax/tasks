FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/investigation

cat > /home/user/investigation/access.log <<'EOF'
192.168.1.101 - - [12/Apr/2024:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 532
203.0.113.4 - - [12/Apr/2024:10:00:05 +0000] "POST /login HTTP/1.1" 401 1001
192.168.1.101 - - [12/Apr/2024:10:01:33 +0000] "GET /dashboard HTTP/1.1" 200 1201
203.0.113.4 - - [12/Apr/2024:10:02:10 +0000] "GET /index.html HTTP/1.1" 200 532
203.0.113.42 - - [12/Apr/2024:10:02:28 +0000] "GET /about HTTP/1.1" 200 800
10.0.0.1 - - [12/Apr/2024:10:02:39 +0000] "GET /admin HTTP/1.1" 403 22

invalid.line.without.ip
192.168.1.101 - - [12/Apr/2024:10:03:10 +0000] "GET /Contact HTTP/1.1" 200 1234
203.0.113.4 - - [12/Apr/2024:10:03:15 +0000] "POST /logout HTTP/1.1" 200 22
203.0.113.42 - - [12/Apr/2024:10:03:44 +0000] "GET /dashboard HTTP/1.1" 404 1200
192.168.1.101 - - [12/Apr/2024:10:04:01 +0000] "GET /index.html HTTP/1.1" 200 532
203.0.113.42 - - [12/Apr/2024:10:04:58 +0000] "GET /index.html HTTP/1.1" 200 532
10.0.0.1 - - [12/Apr/2024:10:05:23 +0000] "GET /stats HTTP/1.1" 200 512
192.168.1.101 - - [12/Apr/2024:10:10:01 +0000] "GET /settings HTTP/1.1" 200 634
203.0.113.4 - - [12/Apr/2024:10:11:02 +0000] "GET /home HTTP/1.1" 200 888

-not.a.valid.ip.address- - - [12/Apr/2024:10:13:13 +0000] "GET /strange HTTP/1.1" 400 333
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
