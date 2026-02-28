#!/bin/bash
if [ -f /home/user/docs/intro.txt ] && [ -f /home/user/docs/summary.txt ] && [ ! -f /home/user/project/intro.txt ] && [ ! -f /home/user/project/summary.txt ] && grep -q "Project Introduction" /home/user/docs/intro.txt && grep -q "Project Summary" /home/user/docs/summary.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
