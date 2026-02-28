#!/bin/bash
set -e
expected='apple
apricot
date
fig
pear'
output=$(sed 's/^\s*//' /home/user/unique.txt | sed '/^$/d')
if [ "$output" = "$expected" ]; then
echo 1 > /logs/verifier/reward.txt
else
echo 0 > /logs/verifier/reward.txt
fi
