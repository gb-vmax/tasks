#!/bin/bash
set -e
cd /home/user

(find /home/user/compliance_symlinks -maxdepth 1 -type l -print0 | while IFS= read -r -d '' f; do echo "$(basename "$f") -> $(readlink "$f")"; done | sort > /home/user/symlink_audit.log)
cat /home/user/symlink_audit.log
