#!/bin/bash
if grep -qx 'MYVAR=hello_export' /home/user/out.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
