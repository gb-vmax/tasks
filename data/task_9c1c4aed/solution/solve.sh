#!/bin/bash
set -e
cd /home/user

cat /home/user/ci/pipeline.yml
sed -i 's/  image: docker:20\.10/  image: docker:24.0/' /home/user/ci/pipeline.yml
sed -i 's/  timeout: 10 minutes/  timeout: 30 minutes/' /home/user/ci/pipeline.yml
cat /home/user/ci/pipeline.yml
printf 'Pipeline Summary\n================\nStages: build, test, deploy\nJobs: build, unit_test, integration_test, deploy_staging\nBuild image: docker:24.0\nBuild timeout: 30 minutes\n' > /home/user/ci/pipeline_summary.txt
cat /home/user/ci/pipeline_summary.txt
