#!/bin/bash
set -e
out=$(lsattr /home/user/file1.txt)
if [[ "$out" == *"file1.txt"* ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
