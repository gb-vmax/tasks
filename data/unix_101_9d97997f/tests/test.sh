#!/bin/bash
set -e
if [ ! -f /home/user/diff_only.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Should only include differing lines, not identical ones
if grep -q 'line one' /home/user/diff_only.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'line two' /home/user/diff_only.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'line four' /home/user/diff_only.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'line three' /home/user/diff_only.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
