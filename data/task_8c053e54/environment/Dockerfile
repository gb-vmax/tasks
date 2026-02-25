FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# No input data files or directories to create for this task
# All files and directories must be created by the agent
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
