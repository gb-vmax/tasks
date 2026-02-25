#!/bin/bash
set -e
cd /home/user

touch /home/user/workflows/deploy.yaml /home/user/workflows/settings.toml
cat > /home/user/workflows/deploy.yaml <<'EOF'
workflows:
  staging_deploy:
    description: "Deploy to staging environment"
    steps:
      - name: build
        command: "./scripts/build.sh"
      - name: test
        command: "./scripts/test.sh"
      - name: deploy
        command: "./scripts/deploy.sh"
EOF
cat > /home/user/workflows/settings.toml <<'EOF'
[staging]
url = "https://staging.example.com"
api_key = "STAGING123ABC"
timeout = 60
EOF
printf "[%s] Edited deploy.yaml\n[%s] Edited settings.toml\n" "$(date '+%F %T')" "$(date '+%F %T')" > /home/user/workflows/config_edit.log
cat /home/user/workflows/deploy.yaml /home/user/workflows/settings.toml /home/user/workflows/config_edit.log
