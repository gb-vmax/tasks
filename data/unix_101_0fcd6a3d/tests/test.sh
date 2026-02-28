#!/bin/bash
start=$(cat /home/user/start_time.txt)
end=$(date +%s)
diff=$((end - start))
if [ "$diff" -ge 2 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
