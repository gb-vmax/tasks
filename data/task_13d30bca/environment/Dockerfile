FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# The initial state only requires /home/user to exist (already created)
# and /home/user/artifact-repo to NOT exist.
# We simply ensure correct ownership of /home/user.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
