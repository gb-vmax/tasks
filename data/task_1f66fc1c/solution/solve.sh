#!/bin/bash
set -e
cd /home/user

cat /home/user/build/build.toml
cat /home/user/build/artifacts.yaml
cat > /home/user/build/build.toml << 'EOF'
[package]
name = "myapp"
version = "2.4.1"
authors = ["build-team@example.com"]

[release]
channel = "stable"
checksum_required = true
target = "linux-x86_64"
EOF
cat > /home/user/build/artifacts.yaml << 'EOF'
version: "2.4.1"
metadata:
  environment: "production"
  owner: "build-team"
artifacts:
  - name: myapp-binary
    path: dist/myapp-2.4.1-linux-x86_64
    type: executable
  - name: myapp-config
    path: dist/myapp-config.tar.gz
    type: archive
EOF
cat /home/user/build/build.toml && echo "---" && cat /home/user/build/artifacts.yaml
