FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if needed
    if ! id user >/dev/null 2>&1; then
        useradd -m user
    fi
    mkdir -p /home/user/localization
    chown -R user:user /home/user/localization

    # Create /home/user/localization/source.txt with required content
    cat > /home/user/localization/source.txt <<EOF
Welcome
Hello
Save
Exit
EOF
    chown user:user /home/user/localization/source.txt
    chmod 644 /home/user/localization/source.txt

    # Create /home/user/localization/old_fr.txt with required content
    cat > /home/user/localization/old_fr.txt <<EOF
Welcome=Bienvenue
Hello=Bonjour
Exit=Sortie
EOF
    chown user:user /home/user/localization/old_fr.txt
    chmod 644 /home/user/localization/old_fr.txt

    # Ensure output files do not exist
    rm -f /home/user/localization/new_fr.txt /home/user/localization/update.log

    # Install pip and pytest
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
