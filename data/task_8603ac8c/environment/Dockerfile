FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/server

cat > /home/user/server/app.log <<'EOF'
2024-05-01 09:31:05 INFO User login successful: user=jane
2024-05-01 09:32:14 ERROR authentication failed for user=smith
2024-05-01 09:33:50 WARN Invalid Password for user=admin
2024-05-01 09:34:17 INFO User logout: user=jane
2024-05-01 09:35:02 ERROR authentication failed for user=alice
2024-05-01 09:36:11 INFO User login successful: user=bob
2024-05-01 09:36:50 WARN Session expired for user=alice
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
