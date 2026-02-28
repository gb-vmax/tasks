#!/bin/bash
set -e
if [ ! -f /home/user/sha256_check_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q "/home/user/filea.txt: OK" /home/user/sha256_check_output.txt && grep -q "/home/user/fileb.txt: OK" /home/user/sha256_check_output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
