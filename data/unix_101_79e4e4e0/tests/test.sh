#!/bin/bash
if [[ -f /home/user/bin/app.sh ]] && cmp -s /home/user/app.sh /home/user/bin/app.sh; then
  perms=$(stat -c '%a' /home/user/bin/app.sh)
  if [[ "$perms" == "750" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
