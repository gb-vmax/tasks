FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# No input data or directories to create for this task
# Do NOT create /home/user/etl_project or any files within it
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
