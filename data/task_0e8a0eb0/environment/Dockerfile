FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create the artifact_manager directory with correct permissions
    mkdir -p /home/user/artifact_manager
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/artifact_manager

    # Write the repos.ini file with the specified content
    cat > /home/user/artifact_manager/repos.ini <<'EOF'
[core]
base_url = https://artifacts.example.org/core
enabled = yes

[testing]
base_url = https://artifacts.example.org/testing
enabled = no

[extra]
base_url = https://artifacts.example.org/extra
enabled = yes

[legacy]
base_url = https://artifacts.example.org/legacy
enabled = no
EOF

    # Set permissions: repos.ini must be user-writeable, world-readable
    chown 1000:1000 /home/user/artifact_manager/repos.ini
    chmod 644 /home/user/artifact_manager/repos.ini

    # Ensure enabled_repos.log does not exist
    rm -f /home/user/artifact_manager/enabled_repos.log
ENDPOST

WORKDIR /home/user
