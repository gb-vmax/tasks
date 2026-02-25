#!/bin/bash
set -e
cd /home/user

ssh-keygen -t ed25519 -C "edge-iot-access" -f /home/user/.ssh/iot_edge_ssh -N ""
chmod 600 /home/user/.ssh/iot_edge_ssh
printf "Key Type: ed25519\nPublic Key Path: /home/user/.ssh/iot_edge_ssh.pub\nPrivate Key Path: /home/user/.ssh/iot_edge_ssh\nComment: edge-iot-access\n" > /home/user/edge_ssh_keygen.log
chown user:user /home/user/.ssh/iot_edge_ssh /home/user/.ssh/iot_edge_ssh.pub /home/user/edge_ssh_keygen.log
cat /home/user/edge_ssh_keygen.log
