#!/bin/bash
set -e
output="$(xz -l /home/user/a.txt.xz /home/user/b.txt.xz)"
if echo "$output" | grep -q "a.txt.xz" && echo "$output" | grep -q "b.txt.xz"; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
