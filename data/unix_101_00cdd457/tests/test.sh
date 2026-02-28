#!/bin/bash
if [ ! -f /home/user/sorted.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
diff <(cat /home/user/sorted.txt) <(printf "apple\nbanana\nkiwi\npear\n") >/dev/null && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
