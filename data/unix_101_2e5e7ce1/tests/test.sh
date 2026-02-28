#!/bin/bash
if grep -q "HOME=" /home/user/env.txt && grep -q "PATH=" /home/user/env.txt; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi
