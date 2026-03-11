#!/bin/bash
set -e
cd /home/user

cat /home/user/accounttool/VERSION
cat /home/user/accounttool/COMMITS
cat /home/user/accounttool/CHANGELOG.md
printf '3.2.0' > /home/user/accounttool/VERSION
printf '\n## v3.2.0\n\n**Features**\n- feat: allow admins to reset user passwords in bulk\n\n**Bug Fixes**\n- fix: correct typo in account suspension email\n- fix: prevent login with expired tokens\n\n**Other**\n- chore: update dependency versions\n- docs: update API reference for user endpoints\n' >> /home/user/accounttool/CHANGELOG.md
cat /home/user/accounttool/VERSION && echo "---" && cat /home/user/accounttool/CHANGELOG.md
cat -A /home/user/accounttool/CHANGELOG.md
sed -i '/^## v3\.2\.0$/i\\' /home/user/accounttool/CHANGELOG.md
cat -A /home/user/accounttool/CHANGELOG.md
