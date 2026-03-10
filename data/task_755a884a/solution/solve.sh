#!/bin/bash
set -e
cd /home/user

cat /home/user/app/VERSION
echo "2.4.8" > /home/user/app/VERSION
cat /home/user/app/CHANGELOG.md
printf '\n## [2.4.8] - 2024-11-15\n\n### Security\n- Patched critical input validation vulnerability in authentication module\n' >> /home/user/app/CHANGELOG.md
cat /home/user/app/VERSION && echo "---" && cat /home/user/app/CHANGELOG.md
