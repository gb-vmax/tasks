FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the CI directory
mkdir -p /home/user/ci

# Create the initial pipeline.yml with the outdated image and low timeout
cat > /home/user/ci/pipeline.yml << 'EOF'
stages:
  - build
  - test
  - deploy

variables:
  REGISTRY: registry.example.com

build:
  stage: build
  image: docker:20.10
  timeout: 10 minutes
  script:
    - docker build -t $REGISTRY/app:$CI_COMMIT_SHA .
    - docker push $REGISTRY/app:$CI_COMMIT_SHA

unit_test:
  stage: test
  image: python:3.11
  timeout: 20 minutes
  script:
    - pip install -r requirements.txt
    - pytest tests/unit

integration_test:
  stage: test
  image: python:3.11
  timeout: 30 minutes
  script:
    - pip install -r requirements.txt
    - pytest tests/integration

deploy_staging:
  stage: deploy
  image: alpine:3.18
  timeout: 15 minutes
  script:
    - ./deploy.sh staging
EOF

# Do NOT create pipeline_summary.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
