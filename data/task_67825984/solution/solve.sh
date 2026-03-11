#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/.config/systemd/user
cat > /home/user/.config/systemd/user/etl-pipeline.service << 'EOF'
[Unit]
Description=ETL Pipeline Job

[Service]
Type=oneshot
ExecStart=/home/user/etl/run_pipeline.sh
EOF
cat > /home/user/.config/systemd/user/etl-pipeline.timer << 'EOF'
[Unit]
Description=Run ETL Pipeline daily at 02:30

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
EOF
systemctl --user enable etl-pipeline.timer
mkdir -p /home/user/.config/systemd/user/timers.target.wants && ln -s /home/user/.config/systemd/user/etl-pipeline.timer /home/user/.config/systemd/user/timers.target.wants/etl-pipeline.timer
echo "=== Service Unit ===" && cat /home/user/.config/systemd/user/etl-pipeline.service && echo && echo "=== Timer Unit ===" && cat /home/user/.config/systemd/user/etl-pipeline.timer && echo && echo "=== Symlink ===" && ls -la /home/user/.config/systemd/user/timers.target.wants/
