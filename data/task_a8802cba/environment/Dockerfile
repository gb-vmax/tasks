FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory
    useradd -m -d /home/user user

    # Ensure /home/user has correct permissions
    chown -R user:user /home/user

    # As user, create the two config files with correct contents
    su - user -c "cat > /home/user/deploy_settings.yaml << 'EOF'
env_variables:
  - name: APP_ENVIRONMENT
    value: development
  - name: DB_HOST
    value: db.example.local
EOF
"

    su - user -c "cat > /home/user/deploy_settings.toml << 'EOF'
[[env_variables]]
name = \"APP_ENVIRONMENT\"
value = \"development\"

[[env_variables]]
name = \"DB_HOST\"
value = \"db.example.local\"
EOF
"

    # Set permissions so that user can read/write the config files
    chown user:user /home/user/deploy_settings.yaml /home/user/deploy_settings.toml
    chmod 644 /home/user/deploy_settings.yaml /home/user/deploy_settings.toml
ENDPOST

WORKDIR /home/user
