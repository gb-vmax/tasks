#!/bin/bash
set -e
cd /home/user

if mv /home/user/deployment_staging/app.tar.gz /home/user/deployment_ready/; then echo "SUCCESS: app.tar.gz moved to deployment_ready" > /home/user/deployment_logs/pipeline.log; else echo "ERROR: app.tar.gz could not be moved" > /home/user/deployment_logs/pipeline.log; fi
cat /home/user/deployment_logs/pipeline.log
