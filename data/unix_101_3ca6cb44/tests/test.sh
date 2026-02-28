#!/bin/bash
if [ ! -f /home/user/all_interfaces.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# The output of ifconfig -a should contain the string 'lo' (the loopback interface) and at least one occurrence of 'flags' or 'mtu'
if grep -q "lo" /home/user/all_interfaces.txt && (grep -q "flags" /home/user/all_interfaces.txt || grep -q "mtu" /home/user/all_interfaces.txt); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
