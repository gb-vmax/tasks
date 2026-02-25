#!/bin/bash
set -euo pipefail

BASE="/home/user/projects/resmon"

# Update version.txt to 1.5.0
printf '1.5.0\n' > "${BASE}/resmon/version.txt"

# Update CHANGELOG.md: prepend new version section before old content
cat > "${BASE}/CHANGELOG.md" << 'EOF'
## [1.5.0] - 2024-06-02
- Added disk I/O statistics collection to the monitoring tool.

## [1.4.2] - 2024-06-01
- Improved resource usage reporting accuracy.
EOF

# Create release log
cat > "${BASE}/reports/release_2024-06-02.log" << 'EOF'
1.5.0
- Added disk I/O statistics collection to the monitoring tool.
Disk I/O statistics monitoring is now available as part of the resource usage tool.
EOF
