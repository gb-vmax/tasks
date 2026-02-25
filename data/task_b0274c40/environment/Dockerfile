FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

    # Ensure user exists
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the required directory structure
    mkdir -p /home/user/projects/i18n

    # Create the en_US.po file with a malicious script tag in the greeting entry and some safe entries
    cat > /home/user/projects/i18n/en_US.po <<EOF
# Sample translation file
msgid "greeting"
msgstr "Welcome to our site! <script>alert('XSS');</script>"

msgid "farewell"
msgstr "Goodbye!"

msgid "info"
msgstr "For help, visit our support page."
EOF

    # Set permissions: en_US.po must be 644 (-rw-r--r--)
    chmod 644 /home/user/projects/i18n/en_US.po

    # Make sure owner is user for all created files/dirs
    chown -R user:user /home/user/projects
ENDPOST

WORKDIR /home/user
