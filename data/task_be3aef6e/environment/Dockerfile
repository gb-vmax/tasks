FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the infra-modules directory
mkdir -p /home/user/infra-modules

# Create the VERSION file with exactly "2.7.4\n"
printf '2.7.4\n' > /home/user/infra-modules/VERSION

# Create the CHANGELOG.md file with the expected content
cat > /home/user/infra-modules/CHANGELOG.md << 'EOF'
# Changelog

## [2.7.4] - 2024-10-30
### Changed
- Updated AWS provider version to 5.x
- Refactored VPC subnet allocation logic

## [2.7.3] - 2024-09-12
### Fixed
- Corrected IAM role ARN output in ECS module
EOF

# Do NOT create RELEASE_NOTES.txt — the agent will create it

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
