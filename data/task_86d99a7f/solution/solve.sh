#!/bin/bash
set -e
cd /home/user

grep -E 'user:(alice|bob) - action:(login|failed|token_refresh) ' /home/user/security/access.log > /home/user/security/old-credentials.log
echo "Old credential entries: $(wc -l < /home/user/security/old-credentials.log)" > /home/user/security/old-credentials-summary.txt
cat /home/user/security/old-credentials-summary.txt
cat /home/user/security/old-credentials.log
