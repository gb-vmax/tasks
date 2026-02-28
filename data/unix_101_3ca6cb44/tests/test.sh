#!/bin/bash
set -e
mtu=$(ip link show eth0 | grep -o 'mtu [0-9]\+' | awk '{print $2}')
if [ "$mtu" = "1400" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
