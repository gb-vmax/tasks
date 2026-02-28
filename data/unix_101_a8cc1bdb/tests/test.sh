#!/bin/bash
last_line=$(tail -n 1 /home/user/logs/event.log)
if [ "$last_line" = '"She said, \"Hello!\""' ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
