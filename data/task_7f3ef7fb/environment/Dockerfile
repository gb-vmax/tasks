FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not already present (for build context)
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi

    # Ensure directory exists and correct permissions
    mkdir -p /home/user/app-deployment
    chown user:user /home/user/app-deployment
    chmod 755 /home/user/app-deployment

    # Create server-list.txt with required content and permissions
    cat > /home/user/app-deployment/server-list.txt <<EOF
app-server-01
web-server-02
db-server-03
backup-server-04
EOF
    chown user:user /home/user/app-deployment/server-list.txt
    chmod 600 /home/user/app-deployment/server-list.txt

    # Create version-info.txt with required content and permissions
    cat > /home/user/app-deployment/version-info.txt <<EOF
app-server-01 2.4.7
web-server-02 3.1.0
db-server-03 1.9.8
EOF
    chown user:user /home/user/app-deployment/version-info.txt
    chmod 600 /home/user/app-deployment/version-info.txt

    # Create deployment.log with required content and permissions
    cat > /home/user/app-deployment/deployment.log <<EOF
2024-03-07 12:15:43 DEPLOY START app-server-01
2024-03-07 12:15:47 DEPLOY START web-server-02
2024-03-07 12:15:51 DEPLOYMENT SUCCEEDED app-server-01
2024-03-07 12:16:05 DEPLOYMENT FAILED web-server-02
2024-03-07 12:17:00 DEPLOY START db-server-03
2024-03-07 12:17:08 DEPLOYMENT SUCCEEDED db-server-03
2024-03-07 12:17:35 DEPLOYMENT SUCCEEDED backup-server-04
2024-03-07 12:18:00 DEPLOYMENT FAILED backup-server-04
2024-03-07 12:18:05 DEPLOYMENT COMPLETE
EOF
    chown user:user /home/user/app-deployment/deployment.log
    chmod 600 /home/user/app-deployment/deployment.log
ENDPOST

WORKDIR /home/user
