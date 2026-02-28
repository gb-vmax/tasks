#!/bin/bash
if grep -q '"name": ".env"' /home/user/tree_output.json && \
   grep -q '"name": ".git"' /home/user/tree_output.json && \
   grep -q '"name": "pre-commit"' /home/user/tree_output.json && \
   grep -q '"name": "banner.jpg"' /home/user/tree_output.json && \
   grep -q '"type": "file"' /home/user/tree_output.json && \
   grep -q '"type": "directory"' /home/user/tree_output.json; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
