FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/docs

cat > /home/user/docs/articles.json <<EOF
{
  "articles": [
    {"id": 1, "title": "Getting Started with Linux", "author": "Alice Smith", "published": true},
    {"id": 2, "title": "Understanding Shell Scripts", "author": "Bob Lee", "published": false},
    {"id": 3, "title": "Mastering JSON Processing", "author": "Cara Zhu", "published": true}
  ]
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
