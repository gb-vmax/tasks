#!/bin/bash
set -e
expected_uid=$(id -u user)
if [ "$(cat /home/user/id_uid.txt)" = "$expected_uid" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
