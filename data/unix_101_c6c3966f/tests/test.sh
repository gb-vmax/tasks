#!/bin/bash
if [ -s /home/user/interfaces.txt ] && grep -q "Iface" /home/user/interfaces.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
