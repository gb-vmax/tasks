FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

install -d -m 755 /home/user/localization

cat > /home/user/localization/en.json <<'EOF'
{
  "login": "Login",
  "logout": "Logout",
  "welcome": "Welcome",
  "profile": "Profile",
  "settings": "Settings"
}
EOF

cat > /home/user/localization/fr.json <<'EOF'
{
  "login": "Connexion",
  "welcome": "Bienvenue",
  "profile": "Profil",
  "extra_fr": "Supplémentaire"
}
EOF

cat > /home/user/localization/es.json <<'EOF'
{
  "login": "Iniciar sesión",
  "logout": "Cerrar sesión",
  "welcome": "Bienvenido",
  "extra_es": "Extra"
}
EOF

# Do NOT create update_report.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
