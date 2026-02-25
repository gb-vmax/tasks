FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not already present (Apptainer mounts host $HOME, but ensure /home/user exists for build-time)
    mkdir -p /home/user/uptime_check
    chown -R root:root /home/user
    chmod 755 /home/user
    chmod 755 /home/user/uptime_check

    # Create status_page_v1.html with given content
    cat > /home/user/uptime_check/status_page_v1.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Site Status</title>
</head>
<body>
    <h1>Website Uptime Monitor</h1>
    <p>Status: Operational</p>
    <p>Last updated: 2024-06-10 15:00 UTC</p>
</body>
</html>
EOF

    # Create status_page_v2.html with given content
    cat > /home/user/uptime_check/status_page_v2.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Site Status</title>
</head>
<body>
    <h1>Website Uptime Monitor</h1>
    <p>Status: <strong>Operational</strong></p>
    <p>Last updated: 2024-06-10 16:00 UTC</p>
    <p>Next scheduled update: 2024-06-11 00:00 UTC</p>
</body>
</html>
EOF

    # Ensure files are owned by root and writable by user (simulate user permissions, since agent is non-root)
    chmod 644 /home/user/uptime_check/status_page_v1.html
    chmod 644 /home/user/uptime_check/status_page_v2.html

    # Install Python3-pip and pytest
    apt-get update
    apt-get install -y python3-pip diffutils patch
    pip3 install pytest
ENDPOST

WORKDIR /home/user
