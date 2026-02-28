#!/bin/bash
if grep -qE '^Iface|^lo|^eth' /home/user/interfaces.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
