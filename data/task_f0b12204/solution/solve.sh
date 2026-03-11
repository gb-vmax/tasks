#!/bin/bash
set -e
cd /home/user

cat /home/user/backups/manifest.json
jq '[.backups[] | select(.size_bytes > 0 and .checksum != null and .status == "complete") | {id, filename}]' /home/user/backups/manifest.json > /home/user/backups/valid_backups.json
apt-get install -y jq
python3 - << 'EOF'
import json

with open('/home/user/backups/manifest.json', 'r') as f:
    data = json.load(f)

backups = data['backups']
total = len(backups)

valid = [
    {"id": entry["id"], "filename": entry["filename"]}
    for entry in backups
    if entry["size_bytes"] > 0 and entry["checksum"] is not None and entry["status"] == "complete"
]

n = len(valid)

with open('/home/user/backups/valid_backups.json', 'w') as f:
    json.dump(valid, f, indent=2)
    f.write('\n')

with open('/home/user/backups/integrity_report.txt', 'w') as f:
    f.write(f'Valid backups: {n}/{total}\n')

print(f"Done. Valid: {n}/{total}")
EOF
cat /home/user/backups/valid_backups.json && echo "---" && cat /home/user/backups/integrity_report.txt
