#!/bin/bash
set -e
cd /home/user

cat /home/user/services/gateway/config.yaml
cat /home/user/services/broker/config.toml
sed -i \
  -e 's/replicas: 2/replicas: 4/' \
  -e 's/tag: v2\.4\.0/tag: v2.5.1/' \
  -e 's/memory: 512Mi/memory: 1024Mi/' \
  /home/user/services/gateway/config.yaml && \
sed -i \
  -e 's/max_connections = 50/max_connections = 200/' \
  -e 's/timeout_seconds = 10/timeout_seconds = 30/' \
  -e 's/enabled = false/enabled = true/' \
  /home/user/services/broker/config.toml
echo "=== /home/user/services/gateway/config.yaml ===" && cat /home/user/services/gateway/config.yaml && echo "" && echo "=== /home/user/services/broker/config.toml ===" && cat /home/user/services/broker/config.toml
