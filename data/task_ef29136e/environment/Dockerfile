FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create storage directory structure
mkdir -p /home/user/storage/appdata
mkdir -p /home/user/storage/logs
mkdir -p /home/user/storage/backups
mkdir -p /home/user/storage/uploads

# Create storage.conf
cat > /home/user/storage/storage.conf << 'EOF'
# Storage monitoring configuration
# format: directory:warning_threshold_mb
/home/user/storage/appdata:50
/home/user/storage/logs:30
/home/user/storage/backups:80
/home/user/storage/uploads:20
EOF

# Create appdata files with dd (so du reports real block usage)
dd if=/dev/zero of=/home/user/storage/appdata/database.db bs=1M count=38 2>/dev/null
dd if=/dev/zero of=/home/user/storage/appdata/cache.bin bs=1M count=14 2>/dev/null
dd if=/dev/zero of=/home/user/storage/appdata/config.json bs=1M count=1 2>/dev/null

# Create logs files
dd if=/dev/zero of=/home/user/storage/logs/app.log bs=1M count=18 2>/dev/null
dd if=/dev/zero of=/home/user/storage/logs/error.log bs=1M count=7 2>/dev/null
dd if=/dev/zero of=/home/user/storage/logs/access.log bs=1M count=3 2>/dev/null

# Create backups files
dd if=/dev/zero of=/home/user/storage/backups/backup_full.tar.gz bs=1M count=60 2>/dev/null
dd if=/dev/zero of=/home/user/storage/backups/backup_inc.tar.gz bs=1M count=22 2>/dev/null

# Create uploads files
dd if=/dev/zero of=/home/user/storage/uploads/image1.png bs=1M count=9 2>/dev/null
dd if=/dev/zero of=/home/user/storage/uploads/image2.png bs=1M count=8 2>/dev/null
dd if=/dev/zero of=/home/user/storage/uploads/document.pdf bs=1M count=4 2>/dev/null

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
