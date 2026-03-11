FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/artifacts

cat > /home/user/artifacts/build_log.txt << 'EOF'
libcore.so
libutils.so
app-release.apk
libcore.so
libnetwork.so
app-release.apk
libcore.so
libutils.so
libnetwork.so
libcore.so
app-debug.apk
libutils.so
libcore.so
app-release.apk
libnetwork.so
libcore.so
app-debug.apk
libutils.so
libcore.so
app-release.apk
libutils.so
libcore.so
libnetwork.so
app-debug.apk
libcore.so
app-release.apk
libutils.so
libnetwork.so
app-debug.apk
app-release.apk
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
