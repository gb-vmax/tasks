#!/bin/bash
if [ -f /home/user/link_to_notes.txt ] && \
   [ "$(stat -c%i /home/user/notes.txt)" = "$(stat -c%i /home/user/link_to_notes.txt)" ] && \
   cmp -s /home/user/notes.txt /home/user/link_to_notes.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
