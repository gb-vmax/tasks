#!/bin/bash
if [ ! -f /home/user/libstuff.a ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
ar t /home/user/libstuff.a | grep -q '^foo.o$' && ar t /home/user/libstuff.a | grep -q '^bar.o$'
if [ $? -eq 0 ]; then
  order=$(ar t /home/user/libstuff.a)
  if [[ "$order" == $'foo.o\nbar.o' ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
