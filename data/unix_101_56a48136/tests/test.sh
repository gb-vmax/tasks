#!/bin/bash
set -e
[ -f /home/user/data.txt.sha256 ] || { echo 0 > /logs/verifier/reward.txt; exit; }
read checksum filename < /home/user/data.txt.sha256
[ "$filename" = "/home/user/data.txt" ] || { echo 0 > /logs/verifier/reward.txt; exit; }
echo -n "Hello SHA256!
" | sha256sum | grep -q "^$checksum " && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
