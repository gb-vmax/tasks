#!/bin/bash
if [ -e /home/user/confidential/report.dat ]; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
