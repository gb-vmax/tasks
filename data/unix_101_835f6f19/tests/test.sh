#!/bin/bash
if [[ $(cat /home/user/page_size.txt) =~ ^[0-9]+$ ]] && [[ $(cat /home/user/page_size.txt) -ge 4096 ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
