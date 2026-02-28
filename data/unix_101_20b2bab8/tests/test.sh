#!/bin/bash
if [[ "$(cat /home/user/story_updated.txt)" == $'The dog sat on the mat.\nA black dog ran away.' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
