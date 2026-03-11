FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/access.log << 'EOF'
2024-06-01T08:12:03Z 192.168.1.10 GET /api/users 200 143
2024-06-01T08:13:45Z 10.0.0.5 POST /api/orders 500 892
2024-06-01T08:15:22Z 172.16.0.3 GET /api/products 200 310
2024-06-01T08:17:09Z 192.168.1.44 DELETE /api/sessions 204 55
2024-06-01T08:19:58Z 10.0.0.8 GET /api/orders 200 415
2024-06-01T08:21:11Z 192.168.1.10 POST /api/users 201 88
2024-06-01T08:23:34Z 172.16.0.9 GET /api/products 503 1203
2024-06-01T08:25:00Z 10.0.0.5 PUT /api/users 200 399
2024-06-01T08:27:17Z 192.168.1.77 GET /api/reports 200 761
2024-06-01T08:29:45Z 10.0.0.8 POST /api/orders 500 512
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
