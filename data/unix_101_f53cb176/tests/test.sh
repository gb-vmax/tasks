#!/bin/bash
if [[ -f /home/user/ipv6_ping_summary.txt ]] && grep -q '3 packets transmitted' /home/user/ipv6_ping_summary.txt && grep -q '3 received' /home/user/ipv6_ping_summary.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
