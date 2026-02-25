FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Create the db_backup directory
mkdir -p /home/user/db_backup

# Ensure correct ownership for the user
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
