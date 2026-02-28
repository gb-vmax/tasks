#!/bin/bash
if grep -q 'user:user:rw-' /home/user/acl.txt && grep -q 'Hello, ACL world!' /home/user/testfile.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
