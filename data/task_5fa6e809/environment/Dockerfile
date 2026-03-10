FROM endless-deps-1e574915063f:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the provisioning directory
mkdir -p /home/user/provisioning

# Create the server_spec.json file
cat > /home/user/provisioning/server_spec.json << 'EOF'
{
  "budget": 50000,
  "rack_units": 42,
  "servers": [
    {"name": "compute-s", "cost": 3000, "ru": 1, "vcpus": 16},
    {"name": "compute-m", "cost": 6000, "ru": 2, "vcpus": 36},
    {"name": "compute-l", "cost": 12000, "ru": 4, "vcpus": 80}
  ]
}
EOF

# Set correct ownership
chown -R user:user /home/user
EOF
ENDSETUP

WORKDIR /home/user
