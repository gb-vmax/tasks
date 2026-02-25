FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

# Create the backup directory if it does not exist
mkdir -p /home/user/backup

# Create the logins.log file with the specified content
cat > /home/user/backup/logins.log <<'EOF'
alice
bob
alice
carol
alice
bob
dan
carol
carol
alice
EOF

# Set permissions: ensure user has read/write access
chmod 600 /home/user/backup/logins.log

# Set ownership to user:user
chown -R user:user /home/user

# Do NOT create login_frequencies.txt or any output files
ENDSETUP

WORKDIR /home/user
