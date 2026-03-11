FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create configs directory with config files
mkdir -p /home/user/configs

cat > /home/user/configs/app.conf << 'EOF'
[server]
host=localhost
port=8080
debug=false
EOF

cat > /home/user/configs/database.conf << 'EOF'
[database]
host=db.internal
port=5432
name=appdb
user=admin
EOF

cat > /home/user/configs/logging.conf << 'EOF'
[logging]
level=INFO
file=/var/log/app.log
max_size=100MB
EOF

# Create backups directory
mkdir -p /home/user/backups

# Create the pre-existing backup.log with one entry
cat > /home/user/backups/backup.log << 'EOF'
configs_v1.tar.gz a3f1c2e4b5d6789012345678901234567890abcdef1234567890abcdef12345678 2048
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
