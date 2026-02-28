#!/bin/bash
set -e
out=$(getfacl /home/user/doc.txt)
echo "$out" | grep -q 'user:alice:r--'
echo "$out" | grep -q 'group:staff:rw-'
echo "$out" | grep -q '# file: /home/user/doc.txt'
echo 1 > /logs/verifier/reward.txt
