#!/bin/bash
ls_path=$(which ls)
if [ -n "$ls_path" ] && [ -x "$ls_path" ] && [[ "$ls_path" == /*/ls ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
