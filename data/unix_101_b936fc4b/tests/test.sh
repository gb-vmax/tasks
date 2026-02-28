#!/bin/bash
if [ -f /home/user/network/tr_no_dns.txt ]; then
  if grep -q 'traceroute to 8.8.8.8' /home/user/network/tr_no_dns.txt && ! grep -E '[a-zA-Z]' /home/user/network/tr_no_dns.txt | grep -q -v 'traceroute to'; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
