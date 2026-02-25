FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/etl_data
touch /home/user/etl_data/data1.csv
touch /home/user/etl_data/data2.csv
touch /home/user/etl_data/data3.csv
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
