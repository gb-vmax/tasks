#!/bin/bash
set -e
cd /home/user

cat /home/user/docs/mkdocs.yml
cat /home/user/docs/site.toml
sed -i 's/site_name: "Procyon Docs v2\.0\.0"/site_name: "Procyon Docs v2.1.0"/' /home/user/docs/mkdocs.yml
sed -i 's/site_description: "Official documentation for Procyon 2\.0\.0"/site_description: "Official documentation for Procyon 2.1.0"/' /home/user/docs/mkdocs.yml
sed -i 's/  version: "2\.0\.0"/  version: "2.1.0"/' /home/user/docs/mkdocs.yml
sed -i 's/  release_stage: "beta"/  release_stage: "stable"/' /home/user/docs/mkdocs.yml
sed -i 's/version = "2\.0\.0"/version = "2.1.0"/' /home/user/docs/site.toml
sed -i 's/last_updated = "2024-09-30"/last_updated = "2024-11-15"/' /home/user/docs/site.toml
sed -i 's/status = "beta"/status = "stable"/' /home/user/docs/site.toml
sed -i 's/output_dir = "dist\/2\.0\.0"/output_dir = "dist\/2.1.0"/' /home/user/docs/site.toml
cat /home/user/docs/mkdocs.yml && echo "---" && cat /home/user/docs/site.toml
