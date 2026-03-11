FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# The tests only require that /home/user exists and that
# /home/user/research/datasets does NOT exist yet.
# No additional setup is needed.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
