FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/accounttool

# Create VERSION file (no trailing newline)
printf '3.1.7' > /home/user/accounttool/VERSION

# Create COMMITS file
cat > /home/user/accounttool/COMMITS << 'EOF'
feat: allow admins to reset user passwords in bulk
fix: correct typo in account suspension email
chore: update dependency versions
fix: prevent login with expired tokens
docs: update API reference for user endpoints
EOF

# Create CHANGELOG.md with initial content (no trailing newline)
printf '## v3.1.6\n\n**Bug Fixes**\n- fix: resolve race condition in session cleanup\n\n**Other**\n- chore: bump lodash to 4.17.21' > /home/user/accounttool/CHANGELOG.md

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
