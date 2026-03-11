#!/bin/bash
set -e
cd /home/user

ls /home/user/webproject
tar -czf /home/user/deploy.tar.gz -C /home/user/webproject index.html style.css app.js
tar -tzf /home/user/deploy.tar.gz > /home/user/archive_contents.txt
mkdir -p /home/user/deployment && tar -xzf /home/user/deploy.tar.gz -C /home/user/deployment
echo "=== Archive Contents ===" && cat /home/user/archive_contents.txt && echo "=== Deployment Directory ===" && ls /home/user/deployment
