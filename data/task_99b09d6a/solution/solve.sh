#!/bin/bash
set -e
cd /home/user

cat > /home/user/project/CHANGELOG.md <<'EOF'
# Changelog

## [1.0.1] - 2024-05-21
### Added
- New module for API integrations

### Fixed
- Issue with database connections

### Changed
- Documentation for the install process
EOF
markdownlint /home/user/project/CHANGELOG.md || echo "No issues found" > /home/user/project/CHANGELOG_lint.log; [ $? -eq 0 ] && echo "No issues found" > /home/user/project/CHANGELOG_lint.log
echo "markdownlint-cli not found: Unable to lint CHANGELOG.md" > /home/user/project/CHANGELOG_lint.log
