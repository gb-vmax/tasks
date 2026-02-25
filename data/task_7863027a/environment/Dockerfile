FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# No input data or directories are required to be created for this task.
# The agent will create /home/user/ml_experiments/artifacts and experiment.log.
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
