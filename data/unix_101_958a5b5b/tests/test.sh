#!/bin/bash
if grep -qE 'Name:\s*example.com' /home/user/result.txt && grep -qE 'Address:' /home/user/result.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
