#!/bin/bash
if ip -br link | grep -qE '^veth1\s+UP'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
