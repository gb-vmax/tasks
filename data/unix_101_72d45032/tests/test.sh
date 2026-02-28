#!/bin/bash
# Cannot directly test sync effect, but can test that files still exist and are unchanged
if [ -f /home/user/testdata/file1.txt ] && [ -f /home/user/testdata/file2.txt ]; then
  grep -q 'Unsaved data' /home/user/testdata/file1.txt && grep -q 'More unsaved data' /home/user/testdata/file2.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
