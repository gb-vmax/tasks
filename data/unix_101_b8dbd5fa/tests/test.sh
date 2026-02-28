#!/bin/bash
if [ -f /home/user/arch_info.txt ] && [ $(wc -l < /home/user/arch_info.txt) -eq 1 ] && [ $(wc -c < /home/user/arch_info.txt) -gt 1 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
