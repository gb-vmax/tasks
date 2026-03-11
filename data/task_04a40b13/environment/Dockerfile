FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/translations

cat > /home/user/translations/fr.po << 'EOF'
# French translations for myapp
# Copyright (C) 2024
msgid ""
msgstr ""
"Project-Id-Version: myapp 2.0\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-06-01 12:00+0000\n"
"PO-Revision-Date: 2024-06-10 09:00+0000\n"
"Last-Translator: Jean Dupont <jean@example.com>\n"
"Language: fr\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"X-Untranslated-Count: 0\n"

msgid "Welcome"
msgstr "Bienvenue"

msgid "Sign in"
msgstr ""

msgid "Sign out"
msgstr "Se déconnecter"

msgid "Username"
msgstr ""

msgid "Password"
msgstr "Mot de passe"

msgid "Forgot password?"
msgstr ""

msgid "Submit"
msgstr "Envoyer"

msgid "Cancel"
msgstr ""

msgid "Save changes"
msgstr "Enregistrer les modifications"

msgid "Delete account"
msgstr ""
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
