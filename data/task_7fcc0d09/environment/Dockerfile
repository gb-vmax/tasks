FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/access.log << 'EOF'
192.168.1.10 - - [15/Mar/2024:10:01:00 +0000] "GET /api/users HTTP/1.1" 404 152 "-" "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:01:05 +0000] "GET /index.html HTTP/1.1" 200 512 "-" "curl/7.68.0"
192.168.1.10 - - [15/Mar/2024:10:01:10 +0000] "POST /api/orders HTTP/1.1" 404 148 "-" "Mozilla/5.0"
10.0.0.5 - - [15/Mar/2024:10:01:15 +0000] "GET /api/products HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
10.0.0.7 - - [15/Mar/2024:10:01:20 +0000] "GET /static/style.css HTTP/1.1" 404 98 "-" "Mozilla/5.0"
10.0.0.5 - - [15/Mar/2024:10:01:25 +0000] "DELETE /api/users/42 HTTP/1.1" 404 140 "-" "curl/7.68.0"
192.168.1.30 - - [15/Mar/2024:10:01:30 +0000] "GET /api/users HTTP/1.1" 500 200 "-" "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:01:35 +0000] "GET /api/orders HTTP/1.1" 404 148 "-" "Mozilla/5.0"
192.168.1.10 - - [15/Mar/2024:10:01:40 +0000] "PUT /api/settings HTTP/1.1" 200 300 "-" "curl/7.68.0"
10.0.0.9 - - [15/Mar/2024:10:01:45 +0000] "GET /api/inventory HTTP/1.1" 404 155 "-" "Mozilla/5.0"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
