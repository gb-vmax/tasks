FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# The initial state requires:
# - /home/user exists and is owned by user:user
# - /home/user/alertsys does NOT exist
# - group 'monitors' does NOT exist
# - users 'alertagent' and 'logreader' do NOT exist

# Ensure /home/user exists and is properly owned
mkdir -p /home/user
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
