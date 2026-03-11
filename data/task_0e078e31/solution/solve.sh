#!/bin/bash
set -e
cd /home/user

ls /home/user/artifacts/
cat /home/user/artifacts/app-core-1.0.sha256
cat /home/user/artifacts/app-ui-2.1.sha256
cat /home/user/artifacts/app-utils-1.4.sha256
sha256sum /home/user/artifacts/app-core-1.0.jar /home/user/artifacts/app-ui-2.1.jar /home/user/artifacts/app-utils-1.4.jar
cat > /home/user/artifacts/verification_report.txt << 'EOF'
Build Artifact Verification Report
===================================
app-core-1.0.jar: OK
app-ui-2.1.jar: CORRUPTED
app-utils-1.4.jar: OK
===================================
Total: 3 | Passed: 2 | Failed: 1
EOF
cat /home/user/artifacts/verification_report.txt
awk 'NR==2 || NR==6 {print length($0), $0}' /home/user/artifacts/verification_report.txt
