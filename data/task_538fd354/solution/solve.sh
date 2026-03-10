#!/bin/bash
set -e
cd /home/user

cat /home/user/deployments/manifest.json
jq '[.[] | select(.status == "ready" and .environment == "production") | {service, version, replicas}]' /home/user/deployments/manifest.json > /home/user/deployments/production_ready.json
python3 -c "
import json

with open('/home/user/deployments/manifest.json') as f:
    manifest = json.load(f)

filtered = [
    {'service': s['service'], 'version': s['version'], 'replicas': s['replicas']}
    for s in manifest
    if s['status'] == 'ready' and s['environment'] == 'production'
]

with open('/home/user/deployments/production_ready.json', 'w') as f:
    json.dump(filtered, f, indent=2)
    f.write('\n')
"
python3 -c "
import json

with open('/home/user/deployments/production_ready.json') as f:
    data = json.load(f)

total = sum(s['replicas'] for s in data)

with open('/home/user/deployments/replica_count.txt', 'w') as f:
    f.write(str(total) + '\n')
"
cat /home/user/deployments/production_ready.json && echo "---" && cat /home/user/deployments/replica_count.txt
