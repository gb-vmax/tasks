#!/bin/bash
set -e
cd /home/user

cat /home/user/operator/VERSION && echo "---" && cat /home/user/operator/pending_commits.txt && echo "---" && cat /home/user/operator/CHANGELOG.md
printf '1.4.0' > /home/user/operator/VERSION
python3 -c "
new_entry = '''## [1.4.0] - 2024-11-15

### Changed
- feat: add leader election support
- fix: handle nil pointer in reconcile loop
- fix: correct RBAC permissions for CRD watcher
- feat: support multi-namespace watch mode

---
'''

with open('/home/user/operator/CHANGELOG.md', 'r') as f:
    existing = f.read()

with open('/home/user/operator/CHANGELOG.md', 'w') as f:
    f.write(new_entry + existing)
"
cat /home/user/operator/VERSION && echo "===" && cat /home/user/operator/CHANGELOG.md
