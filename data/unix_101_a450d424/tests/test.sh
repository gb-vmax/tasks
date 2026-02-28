#!/bin/bash
expected="SGVsbG8sIEJhc2U2NCBlbmNvZGluZyEK"
actual=$(cat /home/user/docs/message.b64 | tr -d '\n')
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
