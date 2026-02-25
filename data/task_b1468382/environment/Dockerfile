FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/uptime_monitor

cat > /home/user/uptime_monitor/VERSION <<EOF
1.4.1
EOF

cat > /home/user/uptime_monitor/CHANGELOG.md <<EOF
## [1.4.1] - 2023-07-01
### Changed
- Improved response time tracking.

## [1.4.0] - 2023-06-25
### Added
- Introduced uptime monitor for service health.
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
