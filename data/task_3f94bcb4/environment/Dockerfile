FROM ubuntu:22.04

ENV PATH="/usr/local/bin:/usr/bin:/bin:$PATH"

RUN <<'ENDPOST'
set -e

    # Install python3-pip, pip, and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and directory structure
    useradd -m user || true

    mkdir -p /home/user/build_logs
    chown -R user:user /home/user/build_logs

    # Create the pipeline.log file with required content
    cat > /home/user/build_logs/pipeline.log <<EOF
[INFO] Starting job 471
[INFO] Checking out source code
[ERROR] Failed to clone repository
[INFO] Build step started
[ERROR] Compilation failed due to missing dependency
[WARNING] Disk space low
[INFO] Running unit tests
[INFO] Unit tests passed
EOF

    chown user:user /home/user/build_logs/pipeline.log
    chmod 644 /home/user/build_logs/pipeline.log
ENDPOST

WORKDIR /home/user
