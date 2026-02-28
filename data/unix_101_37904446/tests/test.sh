#!/bin/bash
if grep -qE '^;; ANSWER SECTION:' /home/user/network/dig_a_example.txt && grep -qE '^example\.com\..*\tA\t' /home/user/network/dig_a_example.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
