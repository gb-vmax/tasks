#!/bin/bash
if [ -f /home/user/locales.txt ] && [ $(wc -l < /home/user/locales.txt) -gt 0 ]; then
  grep -q "C" /home/user/locales.txt && grep -q "POSIX" /home/user/locales.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
