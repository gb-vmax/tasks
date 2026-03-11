FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the api-client directory
mkdir -p /home/user/api-client

# Create the VERSION file with initial version 2.3.7
cat > /home/user/api-client/VERSION << 'EOF'
2.3.7
EOF

# Create the CHANGELOG.md with initial content
cat > /home/user/api-client/CHANGELOG.md << 'EOF'
## [2.3.7] - 2024-05-30

### Fixed
- Timeout handling on slow connections

## [2.3.6] - 2024-05-10

### Added
- Support for custom headers per request
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
