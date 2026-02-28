#!/bin/bash
OUTPUT=$(file /home/user/docs/notes.txt)
if [[ "$OUTPUT" == "/home/user/docs/notes.txt: ASCII text"* || "$OUTPUT" == "/home/user/docs/notes.txt: UTF-8 Unicode text"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
