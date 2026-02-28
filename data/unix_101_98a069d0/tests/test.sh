#!/bin/bash
result=$(cat /home/user/sin_result.txt | tr -d '[:space:]')
# bc -l s(1) gives about 0.84147098480789650665
if [[ "$result" == 0.8414709848* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
