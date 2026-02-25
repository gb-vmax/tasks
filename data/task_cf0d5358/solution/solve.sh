#!/bin/bash
set -e
cd /home/user

sed -i '0,/^# Version: /s/^# Version: .*/# Version: 1.3.0/' /home/user/alert_scripts/check_disk.sh
DATE=$(date -u +%F); ENTRY="## [1.3.0] - $DATE
### Added
- Initial alert email integration.
"; if [ -f /home/user/alert_scripts/CHANGELOG.md ]; then tail -c +1 /home/user/alert_scripts/CHANGELOG.md > /home/user/alert_scripts/.changelog_tmp; printf "%s\n" "$ENTRY" > /home/user/alert_scripts/CHANGELOG.md; cat /home/user/alert_scripts/.changelog_tmp >> /home/user/alert_scripts/CHANGELOG.md; rm /home/user/alert_scripts/.changelog_tmp; else printf "%s\n" "$ENTRY" > /home/user/alert_scripts/CHANGELOG.md; fi
printf "Bumped version to 1.3.0\nChangelog updated for 1.3.0\nRelease prepared successfully\n" > /home/user/alert_scripts/release.log
chmod u+rw /home/user/alert_scripts/check_disk.sh /home/user/alert_scripts/CHANGELOG.md /home/user/alert_scripts/release.log
