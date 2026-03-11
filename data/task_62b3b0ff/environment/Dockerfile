FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the registry directory
mkdir -p /home/user/registry

# Create the image manifest TSV file
cat > /home/user/registry/image_manifest.tsv << 'EOF'
auth-service	v2.1.0	debian:stretch	alice	142
payment-service	v3.0.1	ubuntu:20.04	carol	98
user-service	v1.0.3	ubuntu:18.04	bob	210
gateway-service	v1.5.2	alpine:3.17	dave	55
notification-service	v4.2.0	debian:stretch	eve	180
order-service	v2.0.0	ubuntu:20.04	frank	134
session-service	v1.1.1	ubuntu:18.04	alice	77
inventory-service	v3.3.3	alpine:3.17	carol	66
EOF

# Do NOT create deprecated_report.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
