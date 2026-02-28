#!/bin/bash
if grep -q 'Usage: logname' /home/user/logname_help.txt && grep -q 'Print the name of the current user.' /home/user/logname_help.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
