FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create home directory and workflows directory
    mkdir -p /home/user/workflows
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/workflows

    # Create the initial build.yml with required content
    cat > /home/user/workflows/build.yml <<EOF
steps:
  - name: checkout
    run: git checkout .
  - name: test
    run: ./test.sh
EOF

    # Ensure correct ownership and permissions
    chown 1000:1000 /home/user/workflows/build.yml
    chmod 644 /home/user/workflows/build.yml
ENDPOST

WORKDIR /home/user
