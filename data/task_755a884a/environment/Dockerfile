FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the app directory
mkdir -p /home/user/app

# Create the VERSION file with the initial version
cat > /home/user/app/VERSION << 'EOF'
2.4.7
EOF

# Create the CHANGELOG.md file with prior entries
cat > /home/user/app/CHANGELOG.md << 'EOF'
# Changelog

## [2.4.7] - 2024-10-30

### Fixed
- Resolved race condition in session cleanup worker

## [2.4.6] - 2024-09-18

### Added
- Support for OAuth2 token refresh flows
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
