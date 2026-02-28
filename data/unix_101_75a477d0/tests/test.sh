#!/bin/bash
EXPECTED='thE qUIck brOwn fOx jUmps OvEr thE lAzy dOg.'
if [[ "$(cat /home/user/output.txt)" == "$EXPECTED" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
