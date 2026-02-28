#!/bin/bash
if [[ $(cat /home/user/output.txt | tr -d '[:space:]') == "20" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
