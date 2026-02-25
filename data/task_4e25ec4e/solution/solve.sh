#!/bin/bash
set -e
cd /home/user

cat /home/user/workflows/base_workflow.yaml
sed -i '/^  test:$/a\
  deploy:\n    runs-on: ubuntu-22.04\n    steps:\n      - name: Print deployment\n        run: echo "Deploying application"\n' /home/user/workflows/base_workflow.yaml
cat /home/user/workflows/base_workflow.yaml
awk '/^jobs:/{print;f=1;next} f && /^  deploy:/{f=0} f{next}1' /home/user/workflows/base_workflow.yaml > /home/user/workflows/tmp_workflow.yaml && echo "  deploy:\n    runs-on: ubuntu-22.04\n    steps:\n      - name: Print deployment\n        run: echo \"Deploying application\"" >> /home/user/workflows/tmp_workflow.yaml && mv /home/user/workflows/tmp_workflow.yaml /home/user/workflows/base_workflow.yaml
cat /home/user/workflows/base_workflow.yaml
printf "jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Run tests\n        run: echo \"Running tests\"\n  deploy:\n    runs-on: ubuntu-22.04\n    steps:\n      - name: Print deployment\n        run: echo \"Deploying application\"\n" > /home/user/workflows/base_workflow.yaml
cat /home/user/workflows/base_workflow.yaml
cat /home/user/workflows/advanced_workflow.toml
printf "\n[job.deploy]\nruns_on = \"ubuntu-22.04\"\n[[job.deploy.steps]]\nname = \"Print deployment\"\nrun = \"echo 'Deploying application'\"\n" >> /home/user/workflows/advanced_workflow.toml
cat /home/user/workflows/advanced_workflow.toml
echo "WORKFLOW CONFIGURATION: COMPLETE" > /home/user/workflows/verification.log
