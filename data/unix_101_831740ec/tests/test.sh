#!/bin/bash
# Should return nonzero (fail) for at least one of the given paths
pathchk --portability /home/user/project/README /home/user/project/verylongfilenameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee /home/user/project/illegal:name 2>/logs/verifier/pathchk_output.txt
if [[ $? -ne 0 ]] && grep -q "/home/user/project/illegal:name" /logs/verifier/pathchk_output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
