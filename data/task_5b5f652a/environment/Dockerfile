FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create the project directory and set permissions
    mkdir -p /home/user/localization_project
    chown -R root:root /home/user
    chmod 755 /home/user
    chmod 755 /home/user/localization_project

    # Create .env.example with the required contents
    cat <<EOF > /home/user/localization_project/.env.example
LANG=en_US
LANGUAGE=en
LC_ALL=en_US.UTF-8
EOF

    # Ensure .env.example is readable and writable by the user
    chmod 644 /home/user/localization_project/.env.example
ENDPOST

WORKDIR /home/user
