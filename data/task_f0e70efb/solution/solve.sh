#!/bin/bash
set -e
cd /home/user

ls /home/user/incident/ && cat /home/user/incident/trusted_checksums.sha256
cd /home/user/incident/ && sha256sum --check trusted_checksums.sha256
cat > /home/user/incident/integrity_report.txt << 'EOF'
INTEGRITY CHECK REPORT
======================
FAILED: configs/crontab
FAILED: configs/sshd_config
OK: configs/hosts
OK: configs/nginx.conf
OK: configs/resolv.conf
EOF
cat /home/user/incident/integrity_report.txt
