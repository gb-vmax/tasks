#!/bin/bash
expected='First Line                                   First   line
Second                                       SECOND
Third line                                   third  line '
if cmp -s <(cat /home/user/alpha_beta_sdiff.txt) <(echo -e "$expected"); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
