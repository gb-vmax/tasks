#!/bin/bash
set -e
cd /home/user

ls /home/user/audit_logs/2024-02/
mkdir -p /home/user/backups
tar -czf /home/user/backups/audit_2024-02.tar.gz -C /home/user/audit_logs 2024-02/
cd /home/user/backups && sha256sum audit_2024-02.tar.gz > audit_2024-02.tar.gz.sha256
cat /home/user/backups/audit_2024-02.tar.gz.sha256
tar -tzf /home/user/backups/audit_2024-02.tar.gz
