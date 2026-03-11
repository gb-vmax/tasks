FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

BASE="/home/user/i18n"

# Create locale directories and files
mkdir -p "$BASE/locales/en_US"
mkdir -p "$BASE/locales/pt_BR"
mkdir -p "$BASE/locales/pt_PT"
mkdir -p "$BASE/locales/fr_FR"
mkdir -p "$BASE/active"

# Create source .po files
cat > "$BASE/locales/en_US/messages.po" << 'EOF'
# English translations
msgid ""
msgstr ""
EOF

cat > "$BASE/locales/pt_BR/messages.po" << 'EOF'
# Brazilian Portuguese translations
msgid ""
msgstr ""
EOF

cat > "$BASE/locales/pt_PT/messages.po" << 'EOF'
# European Portuguese translations
msgid ""
msgstr ""
EOF

cat > "$BASE/locales/fr_FR/messages.po" << 'EOF'
# French translations
msgid ""
msgstr ""
EOF

# Create symlinks in active/
# english.po → wrong target (fr_FR)
ln -s "../locales/fr_FR/messages.po" "$BASE/active/english.po"

# portuguese.po → broken symlink (pt doesn't exist)
ln -s "../locales/pt/messages.po" "$BASE/active/portuguese.po"

# french.po → correct target
ln -s "../locales/fr_FR/messages.po" "$BASE/active/french.po"

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
