#!/bin/bash
set -e
cd /home/user

cat /home/user/provisioning/server.conf.tmpl
sed \
  -e 's/{{HOSTNAME}}/prod-web-04/g' \
  -e 's/{{IP_ADDRESS}}/10.0.1.44/g' \
  -e 's/{{MAX_CONNECTIONS}}/512/g' \
  -e 's/{{TIMEOUT_SECONDS}}/30/g' \
  -e 's/{{ENVIRONMENT}}/production/g' \
  /home/user/provisioning/server.conf.tmpl > /home/user/provisioning/server.conf
cat /home/user/provisioning/server.conf
cat /home/user/provisioning/server.conf.tmpl
