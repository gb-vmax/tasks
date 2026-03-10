FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the servers directory
mkdir -p /home/user/servers

# Create the inventory JSON file
cat > /home/user/servers/inventory.json << 'EOF'
[
  {"hostname": "storage01", "ip_address": "10.0.1.50", "os": "Ubuntu 22.04", "cpu_cores": 8, "ram_gb": 64, "status": "active", "datacenter": "us-east-1"},
  {"hostname": "web03", "ip_address": "10.0.0.3", "os": "CentOS 7", "cpu_cores": 2, "ram_gb": 8, "status": "maintenance", "datacenter": "us-west-2"},
  {"hostname": "db01", "ip_address": "10.0.2.10", "os": "Ubuntu 20.04", "cpu_cores": 16, "ram_gb": 128, "status": "active", "datacenter": "us-east-1"},
  {"hostname": "web01", "ip_address": "10.0.0.1", "os": "Ubuntu 22.04", "cpu_cores": 4, "ram_gb": 16, "status": "active", "datacenter": "us-west-2"},
  {"hostname": "web02", "ip_address": "10.0.0.2", "os": "Ubuntu 22.04", "cpu_cores": 4, "ram_gb": 16, "status": "inactive", "datacenter": "eu-central-1"},
  {"hostname": "cache01", "ip_address": "10.0.3.20", "os": "Debian 11", "cpu_cores": 4, "ram_gb": 32, "status": "active", "datacenter": "eu-central-1"}
]
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
