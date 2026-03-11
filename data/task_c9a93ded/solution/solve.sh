#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/check_apk_sizes.py
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
        size_kb = size_bytes // 1024
        total_kb += size_kb
        print("%s: %d KB" % (apk, size_kb))

    print("---")
    print("Total: %d KB" % total_kb)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: check_apk_sizes.py <apk_dir>")
        sys.exit(1)
    get_apk_sizes(sys.argv[1])
EOF
python3 /home/user/pipeline/check_apk_sizes.py /home/user/pipeline/apks/ > /home/user/pipeline/size_report.txt
cat /home/user/pipeline/size_report.txt
