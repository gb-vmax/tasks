#!/bin/bash
if [ -f /home/user/extracted/README.md ] && [ -f /home/user/extracted/src/test.py ]; then
  grep -q 'Project README' /home/user/extracted/README.md && grep -q 'print' /home/user/extracted/src/test.py && echo 1 > /logs/verifier/reward.txt && exit 0
fi
echo 0 > /logs/verifier/reward.txt
