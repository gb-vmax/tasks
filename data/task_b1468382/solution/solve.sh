#!/bin/bash
set -e
cd /home/user

echo "1.4.2" > /home/user/uptime_monitor/VERSION && (printf '## [1.4.2] - 2023-08-10\n### Fixed\n- Corrected bug in downtime duration calculation.\n\n'; cat /home/user/uptime_monitor/CHANGELOG.md) > /home/user/uptime_monitor/CHANGELOG.md.tmp && mv /home/user/uptime_monitor/CHANGELOG.md.tmp /home/user/uptime_monitor/CHANGELOG.md && head -n 6 /home/user/uptime_monitor/CHANGELOG.md && cat /home/user/uptime_monitor/VERSION
