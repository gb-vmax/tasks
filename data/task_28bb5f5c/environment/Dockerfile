FROM endless-deps-87d163a8074d:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the datasets_project directory (empty, no venv, no requirements.txt)
mkdir -p /home/user/datasets_project

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
