#!/bin/bash
date +%s > /home/user/end_time2.txt
start=$(cat /home/user/start_time2.txt)
end=$(cat /home/user/end_time2.txt)
diff=$((end - start))
if [ "$diff" -ge 65 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
