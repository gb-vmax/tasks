FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create required directories
    mkdir -p /home/user/kube-manifests/logs
    mkdir -p /home/user/kube-manifests/reports

    # Set permissions so agent (non-root) can write/read as needed
    chmod -R 0777 /home/user/kube-manifests

    # Create deploy_onboarding.log with required contents
    cat > /home/user/kube-manifests/logs/deploy_onboarding.log <<EOF
2024-06-14 09:55:00 INFO starting deployment pipeline
2024-06-14 09:56:00 ERROR could not pull image registry.example.com/base:latest
2024-06-14 09:57:00 WARNING service endpoint deprecated
2024-06-14 09:58:23 ERROR pod crashloop detected for app-backend
2024-06-14 09:59:00 INFO validating resources
2024-06-14 09:59:45 ERROR could not pull image registry.example.com/base:latest
2024-06-14 10:00:12 INFO deployment completed
2024-06-14 10:01:00 ERROR insufficient permissions to modify resource
2024-06-14 10:02:13 ERROR insufficient permissions to modify resource
2024-06-14 10:03:00 ERROR could not pull image registry.example.com/base:latest
2024-06-14 10:03:42 INFO completed onboarding
2024-06-14 10:03:59 ERROR pod crashloop detected for app-backend
EOF

    # Ensure the created log file is readable
    chmod 0666 /home/user/kube-manifests/logs/deploy_onboarding.log
ENDPOST

WORKDIR /home/user
