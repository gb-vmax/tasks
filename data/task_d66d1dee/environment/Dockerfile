FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/policy

cat > /home/user/policy/benchmark.json << 'EOF'
[
  {"control_id": "CIS-1.1", "description": "Ensure password expiry is 90 days or less", "threshold": 90, "operator": "lte"},
  {"control_id": "CIS-1.2", "description": "Ensure minimum password length is 12 or more", "threshold": 12, "operator": "gte"},
  {"control_id": "CIS-2.1", "description": "Ensure SSH MaxAuthTries is 4 or less", "threshold": 4, "operator": "lte"},
  {"control_id": "CIS-2.2", "description": "Ensure SSH protocol version is 2", "threshold": 2, "operator": "gte"},
  {"control_id": "CIS-3.1", "description": "Ensure core dump hard limit is 0", "threshold": 0, "operator": "lte"}
]
EOF

cat > /home/user/policy/scan_results.json << 'EOF'
[
  {"control_id": "CIS-1.1", "value": 120},
  {"control_id": "CIS-1.2", "value": 14},
  {"control_id": "CIS-2.1", "value": 3},
  {"control_id": "CIS-2.2", "value": 2},
  {"control_id": "CIS-3.1", "value": 0}
]
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
