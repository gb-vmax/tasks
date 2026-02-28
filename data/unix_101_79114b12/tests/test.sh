#!/bin/bash
set -e
cd /home/user
# Should produce multiple files named chunk00, chunk01, ...
# Check that at least chunk00 and chunk01 exist
[ -f chunk00 ] && [ -f chunk01 ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# All output files should be <= 25 bytes
for f in chunk*; do [ "$(stat -c%s "$f")" -le 25 ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }; done
# When concatenated, should match original
cat chunk* | diff - data.csv || { echo 0 > /logs/verifier/reward.txt; exit 0; }
echo 1 > /logs/verifier/reward.txt
