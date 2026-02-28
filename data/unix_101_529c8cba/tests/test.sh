#!/bin/bash
set -e
if [ ! -f /home/user/verify_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -qE '^/home/user/alpha.txt: OK$' /home/user/verify_output.txt && grep -qE '^/home/user/beta.txt: OK$' /home/user/verify_output.txt && [ "$(grep -c ': OK$' /home/user/verify_output.txt)" -eq 2 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
