#!/bin/bash
if grep -E '^[tcpud]+\s+\d+\s+\d+\s+[0-9.]+:[0-9]+' /home/user/listen_numeric.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
