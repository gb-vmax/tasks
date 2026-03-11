#!/bin/bash
set -e
cd /home/user

cat /home/user/docs/site_config.toml
cat /home/user/docs/metadata.yaml
sed -i 's/version = "2.3.1"/version = "2.4.0"/' /home/user/docs/site_config.toml && sed -i 's/status = "beta"/status = "stable"/' /home/user/docs/site_config.toml && sed -i 's/draft = true/draft = false/' /home/user/docs/site_config.toml
sed -i 's/  version: "2.3.1"/  version: "2.4.0"/' /home/user/docs/metadata.yaml && sed -i 's/  stage: "beta"/  stage: "stable"/' /home/user/docs/metadata.yaml && sed -i 's/  last_updated: "2024-03-15"/  last_updated: "2024-06-01"/' /home/user/docs/metadata.yaml
cat /home/user/docs/site_config.toml && echo "---" && cat /home/user/docs/metadata.yaml
