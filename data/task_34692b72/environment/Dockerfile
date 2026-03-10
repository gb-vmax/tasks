FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/analysis

cat > /home/user/analysis/access.log << 'EOF'
192.168.1.1 - - [10/Oct/2024:13:55:36 -0700] "GET /admin/login HTTP/1.1" 200 512
10.0.0.7 - - [10/Oct/2024:13:55:37 -0700] "GET /phpmyadmin HTTP/1.1" 404 209
EOF

cat > /home/user/analysis/scan_log.py << 'EOF'
#!/usr/bin/env python3
import re

log_path = "/home/user/analysis/access.log"

counts = {}
with open(log_path) as f:
    for line in f:
        m = re.match(r'(\S+) .* "(\S+) (\S+) HTTP', line)
        if m:
            ip, method, path = m.group(1), m.group(2), m.group(3)
            key = (ip, path)
            counts[key] = counts.get(key, 0) + 1

print("=== Suspicious Request Scanner v1.0 ===")
print("Scanning log file: /home/user/analysis/access.log")

found = False
for (ip, path), count in sorted(counts.items()):
    if count >= 1:
        print(f"SUSPICIOUS {ip} {count} requests to {path}")
        found = True

if not found:
    print("No suspicious entries found.")
print("=== Scan complete ===")
EOF

chmod +x /home/user/analysis/scan_log.py

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
