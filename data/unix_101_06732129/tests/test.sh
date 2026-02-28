#!/bin/bash
if [ -f /home/user/note.txt.xz ] && [ ! -f /home/user/note.txt ]; then
  xz -d /home/user/note.txt.xz
  if grep -q 'This is a note.' /home/user/note.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
