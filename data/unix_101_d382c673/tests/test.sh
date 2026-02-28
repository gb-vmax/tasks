#!/bin/bash
if grep -q '^2c$' /home/user/easymerge.ed && grep -q '^BY$' /home/user/easymerge.ed && grep -q '^\.$' /home/user/easymerge.ed; then
  if ! grep -q 'CX' /home/user/easymerge.ed; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
