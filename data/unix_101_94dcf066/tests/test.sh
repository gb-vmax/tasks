#!/bin/bash
# zcat --test should exit 0 and not output anything for a good file
if zcat --test /home/user/data.txt.gz >/tmp/test_zcat_stdout 2>/tmp/test_zcat_stderr; then
  if [ ! -s /tmp/test_zcat_stdout ] && [ ! -s /tmp/test_zcat_stderr ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
