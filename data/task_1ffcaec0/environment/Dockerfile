FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Make sure integration_tests directory exists with correct permissions
    mkdir -p /home/user/integration_tests
    chown user:user /home/user/integration_tests
    chmod 700 /home/user/integration_tests

    # Create the legacy_api_test.py script with specified contents
    cat > /home/user/integration_tests/legacy_api_test.py <<'EOF'
print("=== Starting Legacy API Integration Test ===")
print("Connecting to API endpoint http://localhost:7000/api/v1/check ...")
print("Status: 200 OK")
print("Payload: {'result':'success','service':'auth'}")
print("=== Test Passed ===")
EOF

    # Set file permissions for the script
    chown user:user /home/user/integration_tests/legacy_api_test.py
    chmod 600 /home/user/integration_tests/legacy_api_test.py

    # Install Python3 and pip if not available
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip

    # Install pytest for the user (system-wide, since agent has no root)
    pip3 install pytest
ENDPOST

WORKDIR /home/user
