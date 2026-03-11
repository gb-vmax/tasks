FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/build

cat > /home/user/build/build.toml << 'EOF'
[package]
name = "myapp"
version = "2.3.9"
authors = ["build-team@example.com"]

[release]
channel = "beta"
target = "linux-x86_64"
EOF

cat > /home/user/build/artifacts.yaml << 'EOF'
version: "2.3.9"
metadata:
  environment: "staging"
  owner: "build-team"
artifacts:
  - name: myapp-binary
    path: dist/myapp-2.3.9-linux-x86_64
    type: executable
  - name: myapp-config
    path: dist/myapp-config.tar.gz
    type: archive
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
