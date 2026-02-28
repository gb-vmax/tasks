#!/bin/bash
if [[ "${GREETING}" == "HelloWorld" ]] && declare -p GREETING 2>/dev/null | grep -q 'declare -r GREETING="HelloWorld"'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
