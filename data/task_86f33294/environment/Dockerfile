FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create deployment directory structure
mkdir -p /home/user/deployments/releases/v2.3.1
mkdir -p /home/user/deployments/releases/v2.4.0

# Create v2.3.1 files
echo "2.3.1" > /home/user/deployments/releases/v2.3.1/version.txt
echo "version=2.3.1" > /home/user/deployments/releases/v2.3.1/app.conf

# Create v2.4.0 files
echo "2.4.0" > /home/user/deployments/releases/v2.4.0/version.txt
echo "version=2.4.0" > /home/user/deployments/releases/v2.4.0/app.conf

# Create the current symlink pointing to v2.3.1 (absolute path)
ln -s /home/user/deployments/releases/v2.3.1 /home/user/deployments/current

# Do NOT create 'previous' symlink or deploy_log.txt — agent will create those

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
