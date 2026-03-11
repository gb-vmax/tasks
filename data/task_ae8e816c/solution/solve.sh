#!/bin/bash
set -e
cd /home/user

ls /home/user/pentest/tools/ && cat /home/user/pentest/manifest.sha256
cd /home/user/pentest/tools && sha256sum nmap_wrapper.sh enum_users.py port_scan.sh vuln_check.py report_gen.sh
cat > /home/user/pentest/integrity_report.txt << 'EOF'
=== TOOLKIT INTEGRITY REPORT ===

OK: enum_users.py
OK: nmap_wrapper.sh
OK: port_scan.sh
TAMPERED: report_gen.sh
OK: vuln_check.py

VERDICT: 1 file(s) failed integrity check.
EOF
cat /home/user/pentest/integrity_report.txt
