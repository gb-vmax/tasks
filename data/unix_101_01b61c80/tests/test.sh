#!/bin/bash
set -e
if [[ -f /home/user/binfile_restored.bin ]]; then
  cmp --silent /home/user/binfile_restored.bin <(printf '\x44\x61\x74\x61\x31\x32\x33') && echo 1 > /logs/verifier/reward.txt && exit 0
fi
echo 0 > /logs/verifier/reward.txt
