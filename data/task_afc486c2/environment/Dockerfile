FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Create user and home if not present
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi

    # Ensure /home/user/artifacts exists with correct permissions
    mkdir -p /home/user/artifacts
    chown user:user /home/user/artifacts

    # Create /home/user/artifacts/build-output.txt with required content
    cat > /home/user/artifacts/build-output.txt <<EOF
artifact42,2024-06-12T16:12:03Z,SUCCESS
artifact43,2024-06-12T16:15:45Z,FAILED
artifact44,2024-06-12T16:17:00Z,SUCCESS
artifact45,2024-06-12T16:18:34Z,MISSING
EOF

    # Create an empty /home/user/artifacts/failed-artifacts.txt
    : > /home/user/artifacts/failed-artifacts.txt

    # Set permissions so user can write to files
    chown user:user /home/user/artifacts/build-output.txt
    chown user:user /home/user/artifacts/failed-artifacts.txt
    chmod 644 /home/user/artifacts/build-output.txt
    chmod 644 /home/user/artifacts/failed-artifacts.txt

    # Ensure artifact-pipeline.log does NOT exist
    rm -f /home/user/artifacts/artifact-pipeline.log

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
