#!/bin/bash
if [ -f /home/user/network/traceroute_localhost.txt ]; then
  if grep -q 'traceroute to 127.0.0.1' /home/user/network/traceroute_localhost.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
