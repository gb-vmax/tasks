#!/bin/bash
if [ ! -d /home/user/foo ] && [ ! -d /home/user/foo/bar ] && [ ! -d /home/user/foo/bar/baz ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
