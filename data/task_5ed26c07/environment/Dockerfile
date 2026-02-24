FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not present
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi

    # Create /home/user/releases directory with correct permissions
    mkdir -p /home/user/releases
    chown user:user /home/user/releases
    chmod 755 /home/user/releases

    # Create the pending_deployments.csv file with required contents
    cat > /home/user/releases/pending_deployments.csv <<EOF
1042,Inventory,2.3.5,2024-07-01,no
1043,Checkout,1.4.1,2024-07-02,yes
1044,Warehouse,1.2.9,2024-07-05,no
EOF

    # Set permissions so agent (user) can read/write in /home/user/releases
    chown user:user /home/user/releases/pending_deployments.csv
    chmod 644 /home/user/releases/pending_deployments.csv

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
