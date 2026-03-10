#!/bin/bash
set -e
cd /home/user

cat /home/user/api-client/VERSION
echo "2.4.0" > /home/user/api-client/VERSION
cat /home/user/api-client/CHANGELOG.md
printf '## [2.4.0] - 2024-06-15\n\n### Added\n- OAuth2 token refresh support\n\n### Fixed\n- GET requests no longer fail when query params are empty\n\n' | cat - /home/user/api-client/CHANGELOG.md > /tmp/CHANGELOG_new.md && mv /tmp/CHANGELOG_new.md /home/user/api-client/CHANGELOG.md
cat /home/user/api-client/VERSION && echo "---" && head -12 /home/user/api-client/CHANGELOG.md
