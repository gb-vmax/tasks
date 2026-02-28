#!/bin/bash
EXPECTED=$'/home/user/files/sizes_si.txt'
if [[ ! -f "$EXPECTED" ]]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
readarray -t lines < "$EXPECTED"
if [[ "${lines[0]}" == "1.0K" && "${lines[1]}" == "2.5M" && "${lines[2]}" == "1.0M" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
