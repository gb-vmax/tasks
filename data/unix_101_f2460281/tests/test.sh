#!/bin/bash
if [ -f /home/user/lscolors.sh ] && grep -q 'LS_COLORS' /home/user/lscolors.sh && grep -q '01;34' /home/user/lscolors.sh && grep -q 'export LS_COLORS' /home/user/lscolors.sh; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
