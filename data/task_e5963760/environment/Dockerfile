FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/builds

cat > /home/user/builds/build_output.log <<'EOF'
INFO: Build started at 2024-05-22 09:00:01
WARNING: Deprecated API used
ERROR: Failed to resolve dependency 'libfoo'
ERROR: Timeout while connecting to repository
ERROR: Failed to resolve dependency 'libfoo'
INFO: Build finished at 2024-05-22 09:00:34
ERROR: Insufficient disk space
EOF

# Ensure no output file exists (do NOT create build_errors_summary.txt)

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
