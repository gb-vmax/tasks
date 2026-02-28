#!/bin/bash
if [ -f /home/user/arch_version.txt ] && grep -qi 'arch' /home/user/arch_version.txt && grep -qi 'coreutils' /home/user/arch_version.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
