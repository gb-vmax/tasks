FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the configs directory
mkdir -p /home/user/configs

# Create database.conf with the required content and permissions 664
cat > /home/user/configs/database.conf << 'EOF'
host=localhost
port=5432
dbname=production
user=admin
password=s3cr3t
EOF

chmod 664 /home/user/configs/database.conf

# Create audit.log with the pre-existing entry
echo "PERMISSION_CHANGE: /home/user/configs/nginx.conf 666->644 by user" > /home/user/configs/audit.log

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
