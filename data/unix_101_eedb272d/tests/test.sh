#!/bin/bash
set -e
file=/home/user/path_steps.txt
[ -f "$file" ] || { echo 0 > /logs/verifier/reward.txt; exit; }
grep -q 'readme.txt' "$file" && grep -q 'demo' "$file" && grep -q 'projects' "$file" && grep -q 'home' "$file" && grep -q 'user' "$file" && [ "$(wc -l < "$file")" -ge 5 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
