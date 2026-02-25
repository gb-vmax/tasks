FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Per test, do NOT create /home/user/user_management or any of its contents

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
