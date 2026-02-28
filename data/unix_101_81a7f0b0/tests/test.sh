#!/bin/bash
set -e
if [ ! -f /home/user/ali_names.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
# All lines in ali_names.txt must start with 'ali' (case-insensitive)
if ! awk '{l=tolower($0); if (substr(l,1,3)!="ali") exit 1}' /home/user/ali_names.txt; then echo 0 > /logs/verifier/reward.txt; exit; fi
# All lines must exist in the original names.txt
while IFS= read -r line; do grep -qx "$line" /home/user/names.txt || { echo 0 > /logs/verifier/reward.txt; exit; }; done < /home/user/ali_names.txt
echo 1 > /logs/verifier/reward.txt
