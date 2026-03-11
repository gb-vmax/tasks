FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/network/configs
mkdir -p /home/user/network/active

# Create core-router.conf
cat > /home/user/network/configs/core-router.conf << 'EOF'
hostname core-router
interface GigabitEthernet0/0
 ip address 10.0.0.1 255.255.255.0
EOF

# Create edge-router.conf
cat > /home/user/network/configs/edge-router.conf << 'EOF'
hostname edge-router
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
EOF

# Create backup-router.conf
cat > /home/user/network/configs/backup-router.conf << 'EOF'
hostname backup-router
interface GigabitEthernet0/0
 ip address 10.0.1.1 255.255.255.0
EOF

# active directory should be empty (no symlinks or files created here)

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
