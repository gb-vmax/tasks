FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/pipeline

cat > /home/user/pipeline/build.log << 'EOF'
[TIMESTAMP] BUILD STARTED: 2024-05-10 08:31:45
[INFO] Initializing build environment
[INFO] Compiled module: core SUCCESS
[INFO] Compiled module: auth SUCCESS
[WARN] Deprecated API usage in NetworkManager.kt
[INFO] Compiled module: payments FAILED
[INFO] Compiled module: ui SUCCESS
[WARN] Using legacy serialization in DataStore.kt
[INFO] Compiled module: notifications SUCCESS
[WARN] Null safety bypass detected in UserSession.kt
[INFO] Compiled module: analytics FAILED
[INFO] Compiled module: sync SUCCESS
[TIMESTAMP] BUILD FINISHED: 2024-05-10 08:44:02
[RESULT] BUILD STATUS: FAILED
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
