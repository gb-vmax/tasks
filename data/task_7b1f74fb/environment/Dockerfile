FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/sql-optimizer

cat > /home/user/sql-optimizer/VERSION <<EOF
1.4.0
EOF

cat > /home/user/sql-optimizer/CHANGELOG.md <<EOF
## [1.4.0] - 2024-05-30
- Initial release.
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
