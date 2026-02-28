#!/bin/bash
if [ -f /home/user/docs/notes.md ] && [ -f /home/user/docs/plan.md ] && [ ! -f /home/user/docs/notes.txt ] && [ ! -f /home/user/docs/plan.txt ] && grep -q 'Meeting notes' /home/user/docs/notes.md && grep -q 'Project plan' /home/user/docs/plan.md && [ -f /home/user/docs/readme.md ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
