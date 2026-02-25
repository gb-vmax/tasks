FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/compliance_symlinks

# Create the required symlinks
ln -sf /etc/app/config.cfg /home/user/compliance_symlinks/app.cfg
ln -sf /var/db/db1.conf /home/user/compliance_symlinks/db.conf
ln -sf /home/user/old/datafile /home/user/compliance_symlinks/legacy.data

# Do NOT create the target for legacy.data; its target must not exist.
# Do NOT create /home/user/symlink_audit.log.

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
