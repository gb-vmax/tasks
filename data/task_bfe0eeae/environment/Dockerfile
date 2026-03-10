FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# The tests require that /home/user/audit does NOT exist
# and no files exist within it. We only need to ensure /home/user exists.
# /home/user already exists as part of the base image setup.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
