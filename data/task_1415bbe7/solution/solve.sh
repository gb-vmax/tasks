#!/bin/bash
set -e
cd /home/user

ls /home/user/artifacts/v2.4.0/
mkdir -p /home/user/backups && tar -czf /home/user/backups/v2.4.0-release.tar.gz -C /home/user/artifacts v2.4.0
cd /home/user/backups && sha256sum v2.4.0-release.tar.gz > v2.4.0-release.tar.gz.sha256
cat /home/user/backups/v2.4.0-release.tar.gz.sha256 && cd /home/user/backups && sha256sum --check v2.4.0-release.tar.gz.sha256
