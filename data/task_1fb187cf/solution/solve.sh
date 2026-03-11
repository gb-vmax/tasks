#!/bin/bash
set -e
cd /home/user

ls /home/user/compliance/
mkdir -p /home/user/backups
tar -czf /home/user/backups/policies.tar.gz -C /home/user/compliance access_policy.yml network_policy.yml secrets_policy.yml
cd /home/user/backups && sha256sum policies.tar.gz > policies.tar.gz.sha256
tar -tzf /home/user/backups/policies.tar.gz
cat /home/user/backups/policies.tar.gz.sha256
