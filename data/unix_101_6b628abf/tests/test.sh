#!/bin/bash
/home/user/envtest.sh > /tmp/env_output.txt
if grep -q hello_world /tmp/env_output.txt; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
