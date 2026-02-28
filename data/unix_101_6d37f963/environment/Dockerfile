FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/data.txt <<EOF
INFO: Started process
ERROR: Failed to load config
WARNING: Disk space low
ERROR: Connection lost
INFO: Process ended
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

