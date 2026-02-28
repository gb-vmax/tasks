#!/bin/bash
fail=0
for f in /home/user/project/src/empty1.py /home/user/project/src/empty2.py /home/user/project/tests/empty_test.py; do
  if [ -e "$f" ]; then fail=1; fi
done
for f in /home/user/project/src/main.py /home/user/project/tests/test_main.py; do
  if [ ! -e "$f" ]; then fail=1; fi
done
if [ $fail -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
