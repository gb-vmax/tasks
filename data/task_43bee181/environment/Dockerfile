FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the translations directory structure
mkdir -p /home/user/translations/de_DE
mkdir -p /home/user/translations/en_US
mkdir -p /home/user/translations/fr_FR
mkdir -p /home/user/translations/es_ES

# Create de_DE/app.po
cat > /home/user/translations/de_DE/app.po << 'EOF'
msgid "hello"
msgstr "Hallo"
EOF

# Create en_US/app.po
cat > /home/user/translations/en_US/app.po << 'EOF'
msgid "hello"
msgstr "Hello"
EOF

# Create en_US/errors.po
cat > /home/user/translations/en_US/errors.po << 'EOF'
msgid "error_not_found"
msgstr "Not found"
EOF

# Create fr_FR/app.po
cat > /home/user/translations/fr_FR/app.po << 'EOF'
msgid "hello"
msgstr "Bonjour"
EOF

# Create es_ES/app.po
cat > /home/user/translations/es_ES/app.po << 'EOF'
msgid "hello"
msgstr "Hola"
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
