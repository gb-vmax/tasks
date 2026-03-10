FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/l10n/versions
mkdir -p /home/user/l10n/active

# Create versioned .po files
cat > /home/user/l10n/versions/de_v3.po << 'EOF'
# German translations v3
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/es_v2.po << 'EOF'
# Spanish translations v2
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/fr_v1.po << 'EOF'
# French translations v1
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/fr_v2.po << 'EOF'
# French translations v2
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/pt_BR_v2.po << 'EOF'
# Brazilian Portuguese translations v2
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/ja_v1.po << 'EOF'
# Japanese translations v1
msgid ""
msgstr ""
EOF

cat > /home/user/l10n/versions/ko_v1.po << 'EOF'
# Korean translations v1
msgid ""
msgstr ""
EOF

# NOTE: pt_BR_v1.po intentionally does NOT exist

# Create pre-existing symlinks in active/
# de.po -> valid symlink
ln -s ../versions/de_v3.po /home/user/l10n/active/de.po

# es.po -> valid symlink
ln -s ../versions/es_v2.po /home/user/l10n/active/es.po

# fr.po -> stale symlink (points to v1, needs updating to v2)
ln -s ../versions/fr_v1.po /home/user/l10n/active/fr.po

# pt_BR.po -> broken symlink (target pt_BR_v1.po does not exist)
ln -s ../versions/pt_BR_v1.po /home/user/l10n/active/pt_BR.po

# ja.po and ko.po should NOT exist yet
# MANIFEST.txt should NOT exist yet

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
