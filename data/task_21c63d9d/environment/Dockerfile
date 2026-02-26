FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

# Create directories
install -d -m 755 /home/user/deployment_staging
install -d -m 755 /home/user/deployment_ready
install -d -m 755 /home/user/deployment_logs

# Create a non-empty app.tar.gz (just any non-empty file; content doesn't matter)
echo "dummy tarball content" > /home/user/deployment_staging/app.tar.gz

# Create a non-empty readme.txt (any text)
echo "This is a deployment staging readme." > /home/user/deployment_staging/readme.txt

# Ensure ready and logs dirs are empty (redundant, but explicit)
rm -f /home/user/deployment_ready/*
rm -f /home/user/deployment_logs/*

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
