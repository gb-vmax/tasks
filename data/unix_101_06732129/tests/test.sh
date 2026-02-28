#!/bin/bash
if [ ! -f /home/user/data.txt.xz ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ -f /home/user/data.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
xz -d /home/user/data.txt.xz
diff /home/user/data.txt <(echo -e 'apple\nbanana\ncherry') >/dev/null && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
