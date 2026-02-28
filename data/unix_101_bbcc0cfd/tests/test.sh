#!/bin/bash
if grep -qE 'Name:\s*example.org' /home/user/exampleorg_dns.txt && grep -qE 'Server:\s*8.8.8.8' /home/user/exampleorg_dns.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
