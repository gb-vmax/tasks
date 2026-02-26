FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs
cat > /home/user/logs/access.log <<EOF
127.0.0.1 - - [22/Apr/2024:10:01:23 +0000] "GET /index.html HTTP/1.1" 200 4523 "-" "Mozilla/5.0"
192.168.1.5 - - [22/Apr/2024:10:02:10 +0000] "GET /notfound.html HTTP/1.1" 404 678 "-" "Mozilla/5.0"
172.16.0.2 - - [22/Apr/2024:10:02:12 +0000] "GET /missing.png HTTP/1.1" 404 321 "-" "curl/7.79.1"
127.0.0.1 - - [22/Apr/2024:10:03:00 +0000] "POST /api/data HTTP/1.1" 200 123 "-" "python-requests/2.25"
10.0.0.2 - - [22/Apr/2024:10:03:34 +0000] "GET /favicon.ico HTTP/1.1" 404 222 "-" "Mozilla/5.0"
10.0.0.3 - - [22/Apr/2024:10:04:11 +0000] "GET /index.html HTTP/1.1" 200 4523 "-" "Mozilla/5.0"
127.0.0.1 - - [22/Apr/2024:10:04:31 +0000] "GET /notfound.html HTTP/1.1" 404 678 "-" "Mozilla/5.0"
EOF
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
