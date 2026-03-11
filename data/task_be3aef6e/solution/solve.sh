#!/bin/bash
set -e
cd /home/user

cat /home/user/infra-modules/VERSION
cat /home/user/infra-modules/CHANGELOG.md
echo '2.7.5' > /home/user/infra-modules/VERSION
python3 -c "
with open('/home/user/infra-modules/CHANGELOG.md', 'r') as f:
    content = f.read()

header = '# Changelog\n'
rest = content[len(header):]

new_entry = '## [2.7.5] - 2024-11-15\n### Changed\n- Bumped patch version for provisioning pipeline release\n'

new_content = header + '\n' + new_entry + rest

with open('/home/user/infra-modules/CHANGELOG.md', 'w') as f:
    f.write(new_content)
"
cat /home/user/infra-modules/CHANGELOG.md
printf 'Release: 2.7.5\nDate: 2024-11-15\nType: patch\nDescription: Bumped patch version for provisioning pipeline release\n' > /home/user/infra-modules/RELEASE_NOTES.txt
cat /home/user/infra-modules/RELEASE_NOTES.txt
cat /home/user/infra-modules/VERSION
