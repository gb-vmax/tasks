#!/bin/bash
expected='LS_COLORS='
dircolors -b /home/user/mycolors.txt > /tmp/testoutput.txt
if grep -q "$expected" /tmp/testoutput.txt && grep -q 'DIR=35' /tmp/testoutput.txt && grep -q 'LINK=36' /tmp/testoutput.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
