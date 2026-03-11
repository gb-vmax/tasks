FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/diagnostics

# Create access.log
cat > /home/user/diagnostics/access.log << 'EOF'
192.168.1.10 - - [15/Mar/2024:09:00:01 +0000] "GET /api/users HTTP/1.1" 200 1523 "-" "curl/7.68.0"
192.168.1.11 - - [15/Mar/2024:09:00:05 +0000] "POST /api/login HTTP/1.1" 200 892 "-" "Mozilla/5.0"
192.168.1.12 - - [15/Mar/2024:09:00:10 +0000] "GET /api/users HTTP/1.1" 200 1523 "-" "curl/7.68.0"
192.168.1.10 - - [15/Mar/2024:09:00:15 +0000] "GET /api/orders HTTP/1.1" 404 312 "-" "curl/7.68.0"
192.168.1.13 - - [15/Mar/2024:09:00:20 +0000] "GET /api/users HTTP/1.1" 200 1523 "-" "Mozilla/5.0"
192.168.1.14 - - [15/Mar/2024:09:00:25 +0000] "DELETE /api/sessions HTTP/1.1" 403 210 "-" "curl/7.68.0"
192.168.1.11 - - [15/Mar/2024:09:00:30 +0000] "GET /api/products HTTP/1.1" 500 98 "-" "Mozilla/5.0"
192.168.1.12 - - [15/Mar/2024:09:00:35 +0000] "GET /api/users HTTP/1.1" 200 1523 "-" "curl/7.68.0"
192.168.1.10 - - [15/Mar/2024:09:00:40 +0000] "POST /api/login HTTP/1.1" 401 150 "-" "curl/7.68.0"
192.168.1.15 - - [15/Mar/2024:09:00:45 +0000] "GET /api/products HTTP/1.1" 200 4410 "-" "Mozilla/5.0"
192.168.1.13 - - [15/Mar/2024:09:00:50 +0000] "GET /api/users HTTP/1.1" 404 312 "-" "curl/7.68.0"
192.168.1.14 - - [15/Mar/2024:09:00:55 +0000] "POST /api/orders HTTP/1.1" 500 98 "-" "Mozilla/5.0"
192.168.1.10 - - [15/Mar/2024:09:01:00 +0000] "GET /api/users HTTP/1.1" 200 1523 "-" "curl/7.68.0"
192.168.1.11 - - [15/Mar/2024:09:01:05 +0000] "GET /api/products HTTP/1.1" 200 4410 "-" "Mozilla/5.0"
192.168.1.12 - - [15/Mar/2024:09:01:10 +0000] "GET /api/sessions HTTP/1.1" 200 654 "-" "curl/7.68.0"
EOF

# Create app.log
cat > /home/user/diagnostics/app.log << 'EOF'
2024-03-15 08:55:01 [INFO] Application starting up
2024-03-15 08:55:03 [INFO] Database connection established
2024-03-15 08:55:10 [INFO] Cache warmed successfully
2024-03-15 09:00:02 [INFO] User 42 logged in
2024-03-15 09:00:16 [WARN] Response time exceeded 200ms for /api/orders
2024-03-15 09:00:31 [ERROR] Unhandled exception in product handler: NullPointerException
2024-03-15 09:00:53 [ERROR] Database query timeout after 30s on table orders
2024-03-15 09:01:07 [WARN] Memory usage at 87%
2024-03-15 09:01:11 [INFO] Scheduled cleanup job completed
2024-03-15 09:01:15 [ERROR] Failed to connect to cache: Connection refused
EOF

# Create syslog
cat > /home/user/diagnostics/syslog << 'EOF'
Mar 15 08:50:01 webserver cron[1423]: (root) CMD (/usr/lib/cron/run-crons)
Mar 15 08:50:12 webserver kernel: NET: Registered PF_INET6 protocol family
Mar 15 08:50:25 webserver systemd[1]: Starting nginx.service
Mar 15 08:50:26 webserver systemd[1]: Started nginx.service
Mar 15 08:51:00 webserver sshd[2201]: Accepted publickey for deploy from 10.0.0.5
Mar 15 08:55:00 webserver cron[1500]: (root) CMD (/usr/bin/backup.sh)
Mar 15 09:00:01 webserver kernel: EXT4-fs error (device sda1): ext4_find_entry
Mar 15 09:00:15 webserver systemd[1]: nginx.service: Main process exited with error
Mar 15 09:00:16 webserver systemd[1]: Failed to start nginx.service
Mar 15 09:00:17 webserver kernel: Out of memory: Kill process 3142
Mar 15 09:00:30 webserver sshd[2350]: error: maximum authentication attempts exceeded
Mar 15 09:01:00 webserver cron[1601]: (root) CMD (/usr/lib/cron/run-crons)
Mar 15 09:01:05 webserver systemd[1]: Reloading nginx.service
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
