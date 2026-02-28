#!/bin/bash
EXPECTED='Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Sed do
eiusmod tempor incididunt ut labore et
dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea
commodo consequat.'
if [[ -f /home/user/data/paragraph_fmt.txt ]] && diff -u <(echo "$EXPECTED") /home/user/data/paragraph_fmt.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
