FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/incident/configs

# Create current (tampered) config files
printf 'worker_processes 4;\nhttp { listen 80; }\n' > /home/user/incident/configs/nginx.conf
printf 'Port 2222\nPermitRootLogin no\n' > /home/user/incident/configs/sshd_config
printf '127.0.0.1 localhost\n' > /home/user/incident/configs/hosts
printf 'nameserver 8.8.8.8\nnameserver 8.8.4.4\n' > /home/user/incident/configs/resolv.conf
printf '*/5 * * * * /usr/bin/backup.sh\n0 3 * * * /usr/bin/cleanup.sh\n' > /home/user/incident/configs/crontab

# Compute SHA256 hashes for the ORIGINAL (pre-tamper) content
HASH_NGINX=$(printf 'worker_processes 4;\nhttp { listen 80; }\n' | sha256sum | cut -d' ' -f1)
HASH_SSHD=$(printf 'Port 22\nPermitRootLogin no\n' | sha256sum | cut -d' ' -f1)
HASH_HOSTS=$(printf '127.0.0.1 localhost\n' | sha256sum | cut -d' ' -f1)
HASH_RESOLV=$(printf 'nameserver 8.8.8.8\nnameserver 8.8.4.4\n' | sha256sum | cut -d' ' -f1)
HASH_CRONTAB=$(printf '*/5 * * * * /usr/bin/backup.sh\n' | sha256sum | cut -d' ' -f1)

# Create the trusted checksum manifest with two-space separator (sha256sum format)
cat > /home/user/incident/trusted_checksums.sha256 << EOF
${HASH_NGINX}  configs/nginx.conf
${HASH_SSHD}  configs/sshd_config
${HASH_HOSTS}  configs/hosts
${HASH_RESOLV}  configs/resolv.conf
${HASH_CRONTAB}  configs/crontab
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
