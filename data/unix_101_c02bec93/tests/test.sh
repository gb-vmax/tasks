#!/bin/bash
set -e
out=$(lsattr -R /home/user/data/)
if [[ "$out" == *"fileA.txt"* && "$out" == *"fileB.txt"* && "$out" == *"fileC.txt"* ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
