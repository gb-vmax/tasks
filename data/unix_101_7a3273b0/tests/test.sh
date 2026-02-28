#!/bin/bash
if [ -f /home/user/dircolors_defaults.txt ] && grep -q '^# Configuration file for dircolors' /home/user/dircolors_defaults.txt && grep -q '^DIR' /home/user/dircolors_defaults.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
