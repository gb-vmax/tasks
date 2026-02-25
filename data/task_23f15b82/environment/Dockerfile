FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# For this task, no input files are required; just ensure permissions.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
