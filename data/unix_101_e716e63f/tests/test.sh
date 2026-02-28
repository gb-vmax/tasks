#!/bin/bash
set -e
if [ ! -f /home/user/names_shuffled.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Check that all original lines appear exactly once
sort /home/user/names.txt > /tmp/orig.txt
sort /home/user/names_shuffled.txt > /tmp/shuf.txt
diff /tmp/orig.txt /tmp/shuf.txt >/dev/null && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
