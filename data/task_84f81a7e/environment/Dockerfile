FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/localization

cat > /home/user/localization/en.json <<EOF
{
  "welcome": "Welcome to our site.",
  "login_message": "Please enter your username and password."
}
EOF

cat > /home/user/localization/fr.json <<EOF
{
  "welcome": "Bienvenue sur notre site.",
  "login_message": "Veuillez entrer votre identifiant et votre mot de passe."
}
EOF

cat > /home/user/localization/de.json <<EOF
{
  "welcome": "Willkommen auf unserer Seite.",
  "login_message": "Bitte geben Sie Ihren Benutzernamen und Ihr Passwort ein."
}
EOF

# Do NOT create update_verification.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
