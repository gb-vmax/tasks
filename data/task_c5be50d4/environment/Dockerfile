FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not already present
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create /home/user/legacy_services directory and set permissions
    mkdir -p /home/user/legacy_services
    chown user:user /home/user/legacy_services
    chmod 755 /home/user/legacy_services

    # Create the CSV file with the required contents
    cat > /home/user/legacy_services/services.csv <<EOF
service_id,service_name,port,owner,legacy_ip,state
1,AuthService,8080,alice,10.10.2.15,active
2,DataProc,9000,bob,10.10.2.30,inactive
3,WebFront,80,carol,10.10.2.45,active
4,Metrics,9100,dave,10.10.2.60,maintenance
5,Billing,8443,erin,10.10.2.75,active
EOF

    chown user:user /home/user/legacy_services/services.csv
    chmod 644 /home/user/legacy_services/services.csv

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
