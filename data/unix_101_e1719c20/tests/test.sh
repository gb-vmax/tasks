#!/bin/bash
if grep -q '{-brown-} {+red+}' /home/user/diff_output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
