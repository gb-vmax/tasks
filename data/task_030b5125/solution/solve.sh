#!/bin/bash
set -e
cd /home/user

ls /home/user/deploy/artifacts/
cd /home/user/deploy/artifacts/ && sha256sum auth-service-2.1.4.tar.gz billing-service-1.8.0.tar.gz gateway-service-3.0.2.tar.gz > /home/user/deploy/checksums.sha256
cat /home/user/deploy/checksums.sha256
cd /home/user/deploy/artifacts/ && sha256sum --check /home/user/deploy/checksums.sha256
