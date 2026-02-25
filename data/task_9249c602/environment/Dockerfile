FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/data

cat > /home/user/data/users.csv <<EOF
username,email,registration_date
john_doe,john@example.com,2021-01-10
jane_smith,jane.smith@example.net,2022-11-02
bob,bob77@webmail.com,2023-03-15
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
