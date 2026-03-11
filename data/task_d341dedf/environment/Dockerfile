FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/containers

cat > /home/user/containers/stats.txt << 'EOF'
CONTAINER_ID   NAME              CPU%    MEM_USAGE/LIMIT       MEM%    NET_I/O         BLOCK_I/O
a1b2c3d4e5f6   api-gateway       12.34%  256MiB / 512MiB       50.00%  1.2MB / 800kB   45MB / 12MB
b2c3d4e5f6a7   auth-service      3.10%   180MiB / 512MiB       35.16%  500kB / 200kB   10MB / 4MB
c3d4e5f6a7b8   payment-service   45.67%  748MiB / 1GiB         73.05%  8.3MB / 5.1MB   200MB / 90MB
d4e5f6a7b8c9   user-service      8.90%   95MiB / 512MiB        18.55%  300kB / 100kB   5MB / 2MB
e5f6a7b8c9d0   order-service     22.11%  410MiB / 512MiB       80.08%  3.4MB / 2.1MB   80MB / 30MB
f6a7b8c9d0e1   notification-svc  1.05%   60MiB / 256MiB        23.44%  100kB / 50kB    2MB / 1MB
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
