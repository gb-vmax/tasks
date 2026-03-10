#!/bin/bash
set -e
cd /home/user

tar -czf /home/user/backups/app-v2.3.1.tar.gz -C /home/user/deployments app-v2.3.1
cd /home/user/backups && sha256sum app-v2.3.1.tar.gz > app-v2.3.1.tar.gz.sha256
ls -lh /home/user/backups/ && echo "---" && cat /home/user/backups/app-v2.3.1.tar.gz.sha256
