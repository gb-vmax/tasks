FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/pipeline

cat > /home/user/pipeline/build_failures.log << 'EOF'
Gradle sync failed
Code signing error
Unit tests failed
Gradle sync failed
Provisioning profile expired
Unit tests failed
Gradle sync failed
Code signing error
NDK version mismatch
Gradle sync failed
Unit tests failed
Provisioning profile expired
Gradle sync failed
Code signing error
NDK version mismatch
Unit tests failed
Gradle sync failed
Provisioning profile expired
Code signing error
Unit tests failed
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
