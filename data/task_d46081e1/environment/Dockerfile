FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not already present
    if ! id user 2>/dev/null; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create the required CSV file with exact content and correct permissions
    cat > /home/user/app_translations.csv <<'EOF'
welcome,Welcome,Bienvenido
goodbye,Goodbye,Adiós
thanks,Thank you,Gracias
EOF
    chown user:user /home/user/app_translations.csv
    chmod 644 /home/user/app_translations.csv

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
