#!/bin/bash
if [ ! -f /home/user/project_size.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
lines=$(wc -l < /home/user/project_size.txt)
if [ "$lines" -ne 1 ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
size=$(awk '{print $1}' /home/user/project_size.txt)
path=$(awk '{print $2}' /home/user/project_size.txt)
if [[ "$size" =~ ^[0-9]+$ ]] && [ "$path" = "/home/user/project" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
