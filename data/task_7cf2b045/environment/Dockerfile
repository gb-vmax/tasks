FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create the user home and security directory
    mkdir -p /home/user/security

    # Create the api_credentials.csv file with the exact required content
    cat > /home/user/security/api_credentials.csv <<EOF
username,apikey
alice,OLD_KEY_12345
bob,BOB_API_KEY_555
carol,CAROL_KEY_6789
EOF

    # Ensure proper permissions so user can write to /home/user/security and its contents
    chmod 755 /home/user
    chmod 755 /home/user/security
    chmod 644 /home/user/security/api_credentials.csv
ENDPOST

WORKDIR /home/user
