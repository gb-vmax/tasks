#!/bin/bash
if [ -d /home/user/data/archive/2023 ] && [ "$(stat -c%a /home/user/data/archive/2023)" = "700" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
