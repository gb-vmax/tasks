#!/bin/bash
if grep -q "/home/user/customman/foo.1" /home/user/foo_man.txt && [[ $(cat /home/user/foo_man.txt) == foo:* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
