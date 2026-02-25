FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3 python3-pip
    pip3 install pytest

    # Create the user and home directory if not present
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi
    mkdir -p /home/user

    # Seed /home/user/server_data.csv
    cat > /home/user/server_data.csv <<EOF
2024-06-01 14:22:38,OK,
2024-06-01 14:23:16,ERROR,Disk full
2024-06-01 14:25:02,ERROR,Network unreachable
2024-06-01 14:26:17,OK,
2024-06-01 14:27:33,ERROR,CPU thermal event
EOF

    # Seed /home/user/error_log.txt
    echo "2024-05-31 09:14:05,ERROR,Filesystem read-only" > /home/user/error_log.txt

    # Set permissions so non-root user can read/write
    chown user:user /home/user/server_data.csv /home/user/error_log.txt
    chmod 644 /home/user/server_data.csv /home/user/error_log.txt
ENDPOST

WORKDIR /home/user
