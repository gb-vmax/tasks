FROM endless-base:latest

RUN <<'ENDPOST'
set -eux

    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the user and directory structure
    mkdir -p /home/user/release_configs
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/release_configs

    # Create /home/user/release_configs/app.yaml with initial content
    cat > /home/user/release_configs/app.yaml <<'EOF'
release: 2.0.1
config:
  debug: false
  port: 8080
EOF

    # Create /home/user/release_configs/database.toml with initial content
    cat > /home/user/release_configs/database.toml <<'EOF'
[connection]
host = "db.internal"
port = 5432
max_active = 20
EOF

    # Set permissions
    chmod 644 /home/user/release_configs/app.yaml
    chmod 644 /home/user/release_configs/database.toml
ENDPOST

WORKDIR /home/user
