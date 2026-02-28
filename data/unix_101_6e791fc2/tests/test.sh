#!/bin/bash
EXPECTED_SUM="$(b2sum /home/user/testdata.txt | awk '{print $1}')"
read SUM NAME < /home/user/checksums.txt
if [[ "$SUM" == "$EXPECTED_SUM" && "$NAME" == "/home/user/testdata.txt" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
