FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the pipeline directory
mkdir -p /home/user/pipeline

# Create the .env file with the required contents
cat > /home/user/pipeline/.env << 'EOF'
# General application settings
APP_NAME=my-pipeline-app
APP_ENV=production

# CI/CD variables
CI_BUILD_DIR=/workspace/build
CI_ARTIFACT_PATH=/tmp/artifacts
CI_API_TOKEN=ghp_xK92mNpQr7sLvT3wYbZd
CI_RETRY_COUNT=3
CI_TIMEOUT=120
CI_DEPLOY_SECRET=s3cr3t-deploy-key-xyz
CI_REGISTRY_URL=registry.internal.example.com
CI_REGISTRY_PASSWORD=hunter2abc

# App database (not CI)
DB_HOST=db.internal
DB_PASSWORD=supersecret123
DB_PORT=5432

CI_PARALLEL_JOBS=8
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
