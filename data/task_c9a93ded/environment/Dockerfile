FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create pipeline directory structure
mkdir -p /home/user/pipeline/apks

# Create the Python 2 script (intentionally broken for Python 3)
cat > /home/user/pipeline/check_apk_sizes.py << 'EOF'
import os
import sys

def get_apk_sizes(apk_dir):
    apk_files = []
    for f in os.listdir(apk_dir):
        if f.endswith('.apk'):
            apk_files.append(f)
    apk_files.sort()

    total_kb = 0
    for apk in apk_files:
        full_path = os.path.join(apk_dir, apk)
        size_bytes = os.path.getsize(full_path)
        size_kb = size_bytes / 1024
        total_kb += size_kb
        print "%s: %d KB" % (apk, size_kb)

    print "---"
    print "Total: %d KB" % total_kb

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: check_apk_sizes.py <apk_dir>"
        sys.exit(1)
    get_apk_sizes(sys.argv[1])
EOF

# Create APK files with exact sizes
dd if=/dev/zero of=/home/user/pipeline/apks/app-debug.apk bs=1024 count=1024 2>/dev/null
dd if=/dev/zero of=/home/user/pipeline/apks/app-release.apk bs=1024 count=2048 2>/dev/null
dd if=/dev/zero of=/home/user/pipeline/apks/app-staging.apk bs=1024 count=512 2>/dev/null

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
