FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/docs

cat > /home/user/docs/mkdocs.yml << 'EOF'
site_name: "Procyon Docs v2.0.0"
site_url: "https://docs.procyon.io"
site_description: "Official documentation for Procyon 2.0.0"
repo_url: "https://github.com/procyon/procyon"
docs_dir: docs
theme:
  name: material
  palette:
    primary: indigo
extra:
  version: "2.0.0"
  release_stage: "beta"
  analytics:
    provider: google
    property: UA-000000-0
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference: api.md
EOF

cat > /home/user/docs/site.toml << 'EOF'
[metadata]
title = "Procyon Documentation"
version = "2.0.0"
last_updated = "2024-09-30"
status = "beta"
author = "Procyon Technical Writing Team"

[build]
output_dir = "dist/2.0.0"
minify = true
search_index = true

[links]
homepage = "https://procyon.io"
support = "https://support.procyon.io"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
