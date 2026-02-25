FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Create the directory structure
install -d -m 755 /home/user/microservices/orderservice

# Create the start.sh file with 755 permissions
install -m 755 /dev/null /home/user/microservices/orderservice/start.sh

# Ensure ownership is correct
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
