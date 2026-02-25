FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
cat > /home/user/app_error.log <<EOF
[2024-06-11 10:45:23] ERROR: Failed to connect to database
[2024-06-11 10:45:24] WARN: Retrying connection
[2024-06-11 10:45:25] INFO: Connection re-established
[2024-06-11 10:47:10] ERROR: Application crashed due to timeout
[2024-06-11 10:47:13] ERROR: Recovery process started
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
