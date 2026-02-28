#!/bin/bash
OUTPUT=$(file --mime-type /home/user/images/photo.jpg)
if [[ "$OUTPUT" == "/home/user/images/photo.jpg: image/jpeg" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
