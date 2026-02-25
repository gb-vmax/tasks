#!/bin/bash
set -e
cd /home/user

sed -i 's/version:[[:space:]]*"2\.3\.4"/version: "2.4.0"/' /home/user/db-backup-utility/config.yaml
{ d=$(date +%F); f=/home/user/db-backup-utility/CHANGELOG.md; tmp=$(mktemp); echo -e "## [2.4.0] - $d\n### Added\n- Implemented automatic backup retention checks with alerting (Reliability Improvement).\n" > "$tmp"; cat "$f" >> "$tmp"; mv "$tmp" "$f"; }
grep '^version:' /home/user/db-backup-utility/config.yaml && cat /home/user/db-backup-utility/CHANGELOG.md
