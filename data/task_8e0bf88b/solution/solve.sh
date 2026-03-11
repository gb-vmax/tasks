#!/bin/bash
set -e
cd /home/user

find /home/user/fileserver -type f | sort
find /home/user/fileserver -type f \( -name "*.tmp" -o -name "*.sh" -o -name "*.report" \) -exec ls -la {} \;
find /home/user/fileserver -type f -name "*.tmp" -mtime +2 -print0 | xargs -0 rm -f
find /home/user/fileserver -type f -name "*.sh" -perm /o+w -print0 | xargs -0 chmod o-w
find /home/user/fileserver -not -path "*/archive/*" -type f -name "*.report" -mtime +2 -print0 | xargs -0 mv -t /home/user/fileserver/archive/
{ echo "=== REMAINING TMP FILES ==="; find /home/user/fileserver -type f -name "*.tmp" -print | sort; echo "=== FIXED SCRIPTS ==="; find /home/user/fileserver -type f -name "*.sh" ! -perm /o+w -print | sort; echo "=== ARCHIVED REPORTS ==="; find /home/user/fileserver/archive -type f -name "*.report" -print | sort; } > /home/user/audit.log
cat /home/user/audit.log
find /home/user/fileserver -type f | sort && echo "---" && ls -la /home/user/fileserver/scripts/
