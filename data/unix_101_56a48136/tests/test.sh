#!/bin/bash
expected="b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9  /home/user/file1.txt"
if [[ -f /home/user/file1.sha256 && "$(cat /home/user/file1.sha256 | tr -d '\r\n')" == "$expected" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
