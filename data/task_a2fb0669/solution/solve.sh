#!/bin/bash
set -e
cd /home/user

ls /home/user/pipelines/
mkdir -p /home/user/artifacts
tar -czf /home/user/artifacts/pipeline_configs.tar.gz -C /home/user/pipelines/ build.yml deploy.yml notify.yml
tar -tzf /home/user/artifacts/pipeline_configs.tar.gz | sed 's|^\./||' | sort > /home/user/artifacts/contents.txt
cat /home/user/artifacts/contents.txt
tar -tzf /home/user/artifacts/pipeline_configs.tar.gz && ls -lh /home/user/artifacts/
