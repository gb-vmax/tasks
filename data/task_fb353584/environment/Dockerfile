FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

cat > /home/user/translations.csv <<EOF
key,en,fr
greeting,Hello,Bonjour
farewell,Goodbye,
welcome,Welcome,Bienvenue
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
