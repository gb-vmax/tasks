FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the scripts directory and the nightly build script
mkdir -p /home/user/scripts

cat > /home/user/scripts/nightly_build.sh << 'EOF'
#!/bin/bash
echo "Building..."
EOF

chmod +x /home/user/scripts/nightly_build.sh

# Ensure the systemd user directory structure exists but NOT the service/timer files
mkdir -p /home/user/.config/systemd/user

# Do NOT create nightly-build.service, nightly-build.timer, or the timers.target.wants symlink
# Those will be created by the agent

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
