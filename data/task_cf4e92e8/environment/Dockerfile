FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create home and user directories
    mkdir -p /home/user

    # Create /home/user/original.conf with specified content
    cat > /home/user/original.conf << 'EOF'
setting1=on
setting2=off
setting3=yes
EOF

    # Create /home/user/updated.conf with specified content
    cat > /home/user/updated.conf << 'EOF'
setting1=on
setting2=off
setting3=yes
setting4=true
setting5=maybe
EOF

    # Set permissions so that user can read/write these files
    chmod 644 /home/user/original.conf
    chmod 644 /home/user/updated.conf
    chown -R 1000:1000 /home/user
ENDPOST

WORKDIR /home/user
