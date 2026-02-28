#!/bin/bash
if [[ $(cat /home/user/env/third_color.txt) == "blue" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
