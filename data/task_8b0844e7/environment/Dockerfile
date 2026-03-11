FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/configs/versions
mkdir -p /home/user/configs/active

# Create versioned config files
echo "# nginx config version 1" > /home/user/configs/versions/nginx.conf.v1
echo "# nginx config version 2" > /home/user/configs/versions/nginx.conf.v2

# Create the symlink pointing to v1 (initial state)
ln -s /home/user/configs/versions/nginx.conf.v1 /home/user/configs/active/nginx.conf

# Do NOT create provision.log — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
