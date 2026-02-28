#!/bin/bash
set -e
[ -f /home/user/sample.hex ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
grep -q 'Hello, Hexdump!' /home/user/sample.hex && grep -q '00000000' /home/user/sample.hex && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
