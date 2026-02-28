#!/bin/bash
if [ ! -f /home/user/net_summary.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that the file contains the expected header line for ifconfig -s output
if grep -q "Iface" /home/user/net_summary.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
