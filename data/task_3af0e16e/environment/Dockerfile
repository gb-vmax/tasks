FROM endless-deps-87d163a8074d:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# The tests require that /home/user exists but /home/user/profiling_env does NOT exist.
# No input files needed — the agent will create the venv and requirements.txt.

# Ensure home directory exists with correct ownership
mkdir -p /home/user
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
