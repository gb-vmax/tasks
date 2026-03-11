FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/docs

cat > /home/user/docs/site_config.toml << 'EOF'
[site]
title = "My Docs"
base_url = "https://docs.example.com"

[release]
version = "2.3.1"
status = "beta"
draft = true

[theme]
name = "default"
highlight = true
EOF

cat > /home/user/docs/metadata.yaml << 'EOF'
title: "Documentation Portal"
author: "Tech Writing Team"
publication:
  version: "2.3.1"
  stage: "beta"
  last_updated: "2024-03-15"
language: "en"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
