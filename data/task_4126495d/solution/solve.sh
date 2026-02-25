#!/bin/bash
set -e
cd /home/user

find /home/user/security_audit/ -maxdepth 1 -type f -exec stat --format='%A %U %G %n' {} \; | while read p u g n; do echo "$p $u $g $(basename "$n")"; done > /home/user/permission_audit_report.txt
cat /home/user/permission_audit_report.txt
