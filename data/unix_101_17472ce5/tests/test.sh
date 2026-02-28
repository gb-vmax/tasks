#!/bin/bash
set -e
if [ ! -f /home/user/pro_words.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
# All lines must start with 'pro'
if ! awk '{if (substr($0,1,3)!="pro") exit 1}' /home/user/pro_words.txt; then echo 0 > /logs/verifier/reward.txt; exit; fi
# All lines must exist in the original words.txt
while IFS= read -r line; do grep -qx "$line" /home/user/words.txt || { echo 0 > /logs/verifier/reward.txt; exit; }; done < /home/user/pro_words.txt
echo 1 > /logs/verifier/reward.txt
