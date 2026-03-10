FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/net_data/captures
mkdir -p /home/user/net_data/logs
mkdir -p /home/user/net_data/configs

# captures: ~200KB total
dd if=/dev/urandom of=/home/user/net_data/captures/traffic1.pcap bs=1K count=100 2>/dev/null
dd if=/dev/urandom of=/home/user/net_data/captures/traffic2.pcap bs=1K count=100 2>/dev/null

# logs: ~60KB total
dd if=/dev/urandom of=/home/user/net_data/logs/syslog.log bs=1K count=40 2>/dev/null
dd if=/dev/urandom of=/home/user/net_data/logs/firewall.log bs=1K count=20 2>/dev/null

# configs: small config files
echo "hostname router1" > /home/user/net_data/configs/router1.conf
echo "hostname router2" > /home/user/net_data/configs/router2.conf

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
