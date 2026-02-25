FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/data_pipeline

cat > /home/user/data_pipeline/raw_customers.csv <<EOF
first_name,last_name,age,city
Alice,Smith,29,San Francisco
Bob,,twenty five,Los Angeles

Charlie,Brown,34,New York
,,,
Dana,Lee,,Seattle
Edward,Jones,43,Boston
,Martinez,28,Miami

EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
