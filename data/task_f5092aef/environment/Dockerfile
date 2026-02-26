FROM endless-base:latest

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory
    useradd -m user || true

    # Create the localization directory
    mkdir -p /home/user/localization

    # Create /home/user/localization/translations.csv with required content
    cat > /home/user/localization/translations.csv <<EOF
key,en,fr
greeting,Hello,Bonjour
farewell,Goodbye,Au revoir
thanks,Thank you,Merci
apology,Sorry,Désolé
welcome,Welcome,Bienvenue
EOF

    # Create /home/user/localization/fr_updates.csv with required content
    cat > /home/user/localization/fr_updates.csv <<EOF
key,fr
greeting,Salut
thanks,Merci beaucoup
EOF

    # Set ownership and permissions so user can write new files in localization/
    chown -R user:user /home/user/localization
    chmod 755 /home/user
    chmod 755 /home/user/localization
    chmod 644 /home/user/localization/translations.csv
    chmod 644 /home/user/localization/fr_updates.csv
ENDPOST

WORKDIR /home/user
