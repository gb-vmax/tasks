FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/localization

# Create en.txt with required lines
cat >/home/user/localization/en.txt <<EOF
greeting=Hello
farewell=Goodbye
question=How are you?
EOF

# Create fr.txt with required lines
cat >/home/user/localization/fr.txt <<EOF
greeting=Bonjour
question=Comment ça va ?
EOF

# Set ownership and permissions
chown -R user:user /home/user/localization
chmod u+w /home/user/localization/en.txt
chmod u+w /home/user/localization/fr.txt
chmod u+w /home/user/localization

# Do NOT create update_log.txt (the agent will create it)
ENDSETUP

WORKDIR /home/user
