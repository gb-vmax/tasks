#!/bin/bash
date +%s > /home/user/end_time.txt
start=$(cat /home/user/start_time.txt)
end=$(cat /home/user/end_time.txt)
diff=$((end - start))
if [ "$diff" -ge 3 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
