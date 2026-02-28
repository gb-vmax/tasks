#!/bin/bash
result=$(whereis mycmd)
has_bin=$(echo "$result" | grep '/home/user/bin/mycmd')
has_src=$(echo "$result" | grep '/home/user/src/mycmd.c')
has_man=$(echo "$result" | grep '/home/user/man/man1/mycmd.1')
if [[ -n "$has_bin" && -n "$has_src" && -n "$has_man" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
