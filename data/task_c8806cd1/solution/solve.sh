#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/pipeline-utils && [ -d /home/user/pipeline-utils/.git ] || git -C /home/user/pipeline-utils init
printf "Pipeline: Android Release\nStatus: Success\n" > /home/user/pipeline-utils/build_status.txt
git -C /home/user/pipeline-utils add build_status.txt && git -C /home/user/pipeline-utils commit -m "Initial build status"
git -C /home/user/pipeline-utils config user.name "Build Engineer" && git -C /home/user/pipeline-utils config user.email "build.engineer@example.com"
git -C /home/user/pipeline-utils add build_status.txt && git -C /home/user/pipeline-utils commit -m "Initial build status"
git -C /home/user/pipeline-utils tag build-v1.0
cd /home/user/pipeline-utils && git rev-parse HEAD > /home/user/pipeline-verification.log && git log -1 --pretty=%s >> /home/user/pipeline-verification.log && cat build_status.txt >> /home/user/pipeline-verification.log && git tag --points-at HEAD >> /home/user/pipeline-verification.log
