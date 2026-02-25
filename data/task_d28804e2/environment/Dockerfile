FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the required directory structure
    mkdir -p /home/user/projects/build_config

    # Set permissions so the agent (non-root) user can write
    chmod -R 0777 /home/user
    chmod -R 0777 /home/user/projects
    chmod -R 0777 /home/user/projects/build_config

    # Create the artifacts.ini file with the required content
    cat > /home/user/projects/build_config/artifacts.ini <<EOF
[artifact_alpha]
name=libfoo.so
type=library
status=release

[artifact_beta]
name=appbar
type=executable
status=staging

[artifact_gamma]
name=pluginbaz.so
type=plugin
status=release
EOF

    chmod 0666 /home/user/projects/build_config/artifacts.ini
ENDPOST

WORKDIR /home/user
