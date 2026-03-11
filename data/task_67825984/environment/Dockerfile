FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ETL script directory and placeholder script
mkdir -p /home/user/etl
cat > /home/user/etl/run_pipeline.sh << 'EOF'
#!/bin/bash
echo "Running ETL pipeline"
EOF
chmod +x /home/user/etl/run_pipeline.sh

# Do NOT create /home/user/.config/systemd/user/ — the agent must create it
# Do NOT create service file, timer file, or symlink — the agent must create them

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
