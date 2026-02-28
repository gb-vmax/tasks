#!/bin/bash
if [ ! -f /home/user/dir_comparison.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Should mention that file1.txt differs, but not file2.txt
grep -q 'file1.txt' /home/user/dir_comparison.txt && ! grep -q 'file2.txt' /home/user/dir_comparison.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
