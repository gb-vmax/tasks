#!/bin/bash
out=$(ip -j -4 addr)
if echo "$out" | grep -q '"local": "10.10.10.1"' && echo "$out" | grep -q '"local": "10.10.10.2"'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
