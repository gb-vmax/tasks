FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/builds

cat > /home/user/builds/nightly.log << 'EOF'
[2024-11-01 02:11:03] [SUCCESS] artifact=libbase-1.0.0.tar.gz size=204800
[2024-11-01 02:11:47] [SUCCESS] artifact=libcore-2.1.0.tar.gz size=104857
[2024-11-01 02:12:30] [FAILED] artifact=libui-3.0.1.tar.gz size=0
[2024-11-01 02:13:15] [SUCCESS] artifact=libnet-1.4.2.tar.gz size=309120
[2024-11-01 02:14:02] [FAILED] artifact=libgfx-5.2.0.tar.gz size=0
[2024-11-01 02:14:48] [SUCCESS] artifact=libio-2.0.0.tar.gz size=153600
[2024-11-01 02:15:33] [FAILED] artifact=libauth-0.9.1.tar.gz size=0
[2024-11-01 02:16:19] [SUCCESS] artifact=libcache-3.1.4.tar.gz size=256000
[2024-11-01 02:17:05] [FAILED] artifact=libparse-4.0.0.tar.gz size=0
[2024-11-01 02:17:50] [SUCCESS] artifact=libsync-1.2.3.tar.gz size=179200
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
