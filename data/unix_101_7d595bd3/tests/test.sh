#!/bin/bash
zdiff -u /home/user/dir/dataA.gz /home/user/dir/dataB.gz > /home/user/zdiff_u_output.txt
# Should be in unified diff format, showing -uniqueA and +uniqueB
if grep -q '^---' /home/user/zdiff_u_output.txt \
  && grep -q '^+++' /home/user/zdiff_u_output.txt \
  && grep -q '^-uniqueA' /home/user/zdiff_u_output.txt \
  && grep -q '^+uniqueB' /home/user/zdiff_u_output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
