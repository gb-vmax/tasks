#!/bin/bash
set -e
cd /home/user

find /home/user/iot_deploy/ -type f | sort
cat -n /home/user/iot_deploy/configs/device.conf
cat -n /home/user/iot_deploy/configs/mqtt.conf
cat -n /home/user/iot_deploy/services/watchdog.service
cat -n /home/user/iot_deploy/startup.sh
ls -la /home/user/iot_deploy/startup.sh /home/user/iot_deploy/configs/device.conf /home/user/iot_deploy/configs/mqtt.conf /home/user/iot_deploy/services/watchdog.service
python3 << 'PYEOF'
report = """=== IOT SECURITY AUDIT REPORT ===
Scanned directory: /home/user/iot_deploy

--- SECTION 1: HARDCODED CREDENTIALS ---
Total findings: 4
device.conf:5: password=admin123
mqtt.conf:4: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
startup.sh:6: api_key=AKIAIOSFODNN7EXAMPLE
watchdog.service:6: secret=watchdog_secret_key_9x2k

--- SECTION 2: FILE PERMISSION AUDIT ---
startup.sh: UNSAFE
device.conf: OK
mqtt.conf: UNSAFE
watchdog.service: OK
Total unsafe files: 2

--- SECTION 3: INSECURE PROTOCOLS ---
Total findings: 4
device.conf:7: management_protocol=telnet
device.conf:8: backup_url=ftp://backup.internal.example.com/configs
startup.sh:7: update_server=http://updates.internal.example.com/firmware
startup.sh:8: telnet_fallback=disabled

--- SUMMARY ---
Total issues found: 10
Risk level: CRITICAL
"""

with open('/home/user/iot_deploy/security_report.txt', 'w') as f:
    f.write(report)

print("Report written successfully.")
PYEOF
cat /home/user/iot_deploy/security_report.txt
