FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/access.log << 'EOF'
203.0.113.5 - - [15/Mar/2024:10:01:00 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
203.0.113.5 - - [15/Mar/2024:10:01:05 +0000] "GET /about.html HTTP/1.1" 200 512 "-" "Mozilla/5.0"
198.51.100.2 - - [15/Mar/2024:10:01:10 +0000] "POST /login HTTP/1.1" 200 256 "-" "curl/7.68"
203.0.113.5 - - [15/Mar/2024:10:01:15 +0000] "GET /contact.html HTTP/1.1" 404 128 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:01:20 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:01:25 +0000] "POST /login HTTP/1.1" 401 64 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:01:30 +0000] "GET /admin HTTP/1.1" 403 96 "-" "BadBot/1.0"
172.16.0.8 - - [15/Mar/2024:10:01:35 +0000] "GET /admin/config HTTP/1.1" 403 96 "-" "BadBot/1.0"
172.16.0.8 - - [15/Mar/2024:10:01:40 +0000] "GET /admin/users HTTP/1.1" 403 96 "-" "BadBot/1.0"
203.0.113.5 - - [15/Mar/2024:10:01:45 +0000] "GET /products.html HTTP/1.1" 200 2048 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:01:50 +0000] "HEAD /index.html HTTP/1.1" 200 0 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:01:55 +0000] "GET /dashboard HTTP/1.1" 200 4096 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:02:00 +0000] "GET /etc/passwd HTTP/1.1" 404 64 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:02:05 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
192.168.1.99 - - [15/Mar/2024:10:02:10 +0000] "GET /style.css HTTP/1.1" 200 768 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:02:15 +0000] "GET /robots.txt HTTP/1.1" 200 128 "-" "wget/1.20"
203.0.113.5 - - [15/Mar/2024:10:02:20 +0000] "POST /contact HTTP/1.1" 200 320 "-" "Mozilla/5.0"
198.51.100.2 - - [15/Mar/2024:10:02:25 +0000] "GET /api/data HTTP/1.1" 500 200 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:02:30 +0000] "POST /login HTTP/1.1" 401 64 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:02:35 +0000] "POST /comment HTTP/1.1" 201 128 "-" "Mozilla/5.0"
203.0.113.5 - - [15/Mar/2024:10:02:40 +0000] "GET /faq.html HTTP/1.1" 200 640 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:02:45 +0000] "GET /sitemap.xml HTTP/1.1" 200 2048 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:02:50 +0000] "DELETE /api/item/5 HTTP/1.1" 204 0 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:02:55 +0000] "GET /wp-admin HTTP/1.1" 403 96 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:03:00 +0000] "GET /blog HTTP/1.1" 200 3200 "-" "Mozilla/5.0"
203.0.113.5 - - [15/Mar/2024:10:03:05 +0000] "GET /news.html HTTP/1.1" 200 1280 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:03:10 +0000] "GET /about.html HTTP/1.1" 404 128 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:03:15 +0000] "POST /api/submit HTTP/1.1" 200 512 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:03:20 +0000] "GET /phpmyadmin HTTP/1.1" 404 64 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:03:25 +0000] "GET /gallery HTTP/1.1" 200 5120 "-" "Mozilla/5.0"
203.0.113.5 - - [15/Mar/2024:10:03:30 +0000] "GET /team.html HTTP/1.1" 200 960 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:03:35 +0000] "HEAD /contact.html HTTP/1.1" 200 0 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:03:40 +0000] "GET /api/users HTTP/1.1" 403 128 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:03:45 +0000] "GET /.env HTTP/1.1" 404 64 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:03:50 +0000] "GET /contact.html HTTP/1.1" 200 512 "-" "Mozilla/5.0"
203.0.113.5 - - [15/Mar/2024:10:03:55 +0000] "GET /careers.html HTTP/1.1" 200 1100 "-" "Mozilla/5.0"
10.0.0.1 - - [15/Mar/2024:10:04:00 +0000] "GET /privacy.html HTTP/1.1" 200 768 "-" "wget/1.20"
198.51.100.2 - - [15/Mar/2024:10:04:05 +0000] "POST /login HTTP/1.1" 401 64 "-" "curl/7.68"
172.16.0.8 - - [15/Mar/2024:10:04:10 +0000] "GET /shell.php HTTP/1.1" 404 64 "-" "BadBot/1.0"
192.168.1.99 - - [15/Mar/2024:10:04:15 +0000] "POST /subscribe HTTP/1.1" 200 256 "-" "Mozilla/5.0"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
