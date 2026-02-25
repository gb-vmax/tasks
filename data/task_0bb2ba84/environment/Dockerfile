FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
# Create user and home directory
    useradd -m user
    mkdir -p /home/user/logs
    chown -R user:user /home/user
    chmod 755 /home/user
    chmod 755 /home/user/logs

    # Create the microservice-app.log file with the specified content
    cat > /home/user/logs/microservice-app.log <<'EOF'
2024-06-21T14:11:03Z auth INFO User logged in: id=74
2024-06-21T14:11:07Z payment ERROR Payment failed: code=500
2024-06-21T14:11:09Z auth WARN Token expired for user: id=74
2024-06-21T14:11:10Z shipping INFO Package sent: id=134
2024-06-21T14:11:14Z payment ERROR Invalid account number: id=315
2024-06-21T14:11:17Z auth ERROR Authentication failed: id=74
2024-06-21T14:11:21Z shipping ERROR API timeout: endpoint=track
EOF
    chown user:user /home/user/logs/microservice-app.log
    chmod 644 /home/user/logs/microservice-app.log

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
