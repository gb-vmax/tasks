#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/infra/backups
tar -czf /home/user/infra/backups/configs_backup.tar.gz -C /home/user/infra configs/
cd /home/user/infra/backups && sha256sum configs_backup.tar.gz > configs_backup.tar.gz.sha256
cd /home/user/infra/backups && cat configs_backup.tar.gz.sha256 && sha256sum --check configs_backup.tar.gz.sha256
