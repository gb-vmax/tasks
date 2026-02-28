#!/bin/bash
expected='ID  Score   Status
1   88      Pass
2   75      Fail
'
if [[ -f /home/user/reports/columns_expanded.txt ]] && diff -u <(printf "$expected") /home/user/reports/columns_expanded.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
