#!/bin/bash
paths=($(which -a echo))
# Should contain /home/user/bin/echo and at least one system echo
if [[ " ${paths[@]} " =~ " /home/user/bin/echo " ]] && [[ "${paths[1]}" == /*/echo ]] && [ -x "/home/user/bin/echo" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
