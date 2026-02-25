FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory
    useradd -m user
    mkdir -p /home/user

    # Create ping_results.log with the specified contents
    cat >/home/user/ping_results.log <<EOF
[2024-06-06 08:31:22] Host: server1.example.com Result: 0% packet loss
[2024-06-06 08:31:23] Host: 192.168.0.42 Result: 100% packet loss
[2024-06-06 08:31:24] Host: 10.0.0.13 Result: 100% packet loss
[2024-06-06 08:31:25] Host: router.local Result: 0% packet loss
[2024-06-06 08:31:26] Host: 172.16.5.9 Result: 100% packet loss
EOF

    # Ensure correct permissions for user access (non-root)
    chown -R user:user /home/user
    chmod 755 /home/user
    chmod 644 /home/user/ping_results.log
ENDPOST

WORKDIR /home/user
