FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create devteam group
groupadd devteam

# Create alice user
useradd -m alice

# Create project directory structure
mkdir -p /home/user/projects/webapp

# Create config.cfg with content and overly permissive mode
echo "db_password=secret" > /home/user/projects/webapp/config.cfg
chmod 0666 /home/user/projects/webapp/config.cfg

# Set webapp directory ownership and permissions
chown user:devteam /home/user/projects/webapp
chmod 0775 /home/user/projects/webapp

# Create tickets directory
mkdir -p /home/user/tickets
chmod 0755 /home/user/tickets

# ticket_042.txt must NOT exist yet (agent will create it)

# Set ownership
chown -R user:user /home/user/projects
chown -R user:user /home/user/tickets
# Re-apply group ownership for webapp
chown user:devteam /home/user/projects/webapp

chown -R user:user /home/user
# Re-apply group ownership for webapp after chown -R
chown user:devteam /home/user/projects/webapp
ENDSETUP

WORKDIR /home/user
