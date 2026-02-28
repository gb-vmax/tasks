#!/bin/bash
set -e
found=0
for d in /home/user/tmpwork/jobtemp_*_data; do
  if [[ "$d" =~ ^/home/user/tmpwork/jobtemp_[A-Za-z0-9]{6}_data$ ]] && [ -d "$d" ]; then
    perms=$(stat -c %A "$d")
    [[ "$perms" == drwx------* || "$perms" == drwxrwx---* || "$perms" == drwxr-x---* ]] && found=1 && break
  fi
done
if [ $found -eq 1 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
