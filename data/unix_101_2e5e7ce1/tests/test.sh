#!/bin/bash
if env FOO=BAR | grep -q '^FOO=BAR$'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
