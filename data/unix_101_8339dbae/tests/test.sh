#!/bin/bash
if [ ! -f /home/user/session_000 ] || [ ! -f /home/user/session_001 ] || [ ! -f /home/user/session_002 ] || [ ! -f /home/user/session_003 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# session_000 should contain only 'Header info'
if [ "$(cat /home/user/session_000)" != "Header info" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# session_001 should start with '=== SESSION START ==='
if ! grep -q '^=== SESSION START ===' /home/user/session_001; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# session_003 should contain last session
if ! grep -q 'User: Eve' /home/user/session_003; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Check suffixes are 3 digits
for f in /home/user/session_000 /home/user/session_001 /home/user/session_002 /home/user/session_003; do [[ $(basename "$f") =~ session_[0-9]{3} ]] || { echo 0 > /logs/verifier/reward.txt; exit 0; }; done
echo 1 > /logs/verifier/reward.txt
