FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# No input data files required for this task.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
