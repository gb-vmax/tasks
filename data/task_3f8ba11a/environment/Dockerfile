FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user 'user' with home directory /home/user
    useradd -m -s /bin/bash user

    # Create /home/user/cicd_logs as 'user', ensure it's writable
    install -d -o user -g user -m 755 /home/user/cicd_logs

    # Create build_log_2024-06-01.txt with required content
    cat <<EOF > /home/user/cicd_logs/build_log_2024-06-01.txt
Build #101: BUILD SUCCESS
Build #102: BUILD FAILED: DependencyError - missing package xyz
Build #103: BUILD SUCCESS
Build #104: BUILD FAILED: TestError - test suite failed
Build #105: BUILD FAILED: DependencyError - missing package xyz
Build #106: BUILD SUCCESS
EOF
    chown user:user /home/user/cicd_logs/build_log_2024-06-01.txt
    chmod 644 /home/user/cicd_logs/build_log_2024-06-01.txt

    # Create build_log_2024-06-02.txt with required content
    cat <<EOF > /home/user/cicd_logs/build_log_2024-06-02.txt
Build #201: BUILD SUCCESS
Build #202: BUILD SUCCESS
Build #203: BUILD FAILED: TimeoutError - build step exceeded time limit
Build #204: BUILD FAILED: DependencyError - missing package xyz
Build #205: BUILD FAILED: TestError - test suite failed
EOF
    chown user:user /home/user/cicd_logs/build_log_2024-06-02.txt
    chmod 644 /home/user/cicd_logs/build_log_2024-06-02.txt
ENDPOST

WORKDIR /home/user
