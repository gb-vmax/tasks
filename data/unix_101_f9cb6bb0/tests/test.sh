#!/bin/bash
expected='Apple,1.20
Orange,0.80'
if [[ -f /home/user/product_prices.csv ]] && diff -u <(echo "$expected") /home/user/product_prices.csv >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
