#!/bin/bash
if alias -p | grep -q "alias ll='ls -l'" && alias -p | grep -q "alias gs='git status'"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
