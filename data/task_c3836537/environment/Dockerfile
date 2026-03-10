FROM endless-deps-abbd7d98be32:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create monitoring directory
mkdir -p /home/user/monitoring

# Create hosts.txt with the expected hostnames in the correct order
cat > /home/user/monitoring/hosts.txt << 'EOF'
localhost
fake-host-one.internal
fake-host-two.internal
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
