#!/bin/bash
shopt -s expand_aliases
alias gotmp='cd /home/user/tmp'
cd /home/user
if [ "$PWD" = "/home/user" ]; then
  gotmp
  if [ "$PWD" = "/home/user/tmp" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
