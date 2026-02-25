FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

cat > /home/user/sample_data.log <<EOF
[2023-03-11 09:10:05] INFO - Import task started
[2023-03-11 09:10:07] ERROR - File not found
[2023-03-11 09:10:12] INFO - Importing record 1/150
[2023-03-11 09:11:01] WARNING - Deprecated API usage
[2023-03-11 09:11:02] INFO - Importing record 2/150
[2023-03-11 09:12:02] ERROR - Connection reset by peer
[2023-03-11 09:13:10] INFO - Import complete
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
