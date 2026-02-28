#!/bin/bash
set -e
link_path="/home/user/docs/summary_link.txt"
if [ ! -L "$link_path" ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that the symlink points to the correct relative path
if [ "$(readlink "$link_path")" = "../summary.txt" ]; then
  # Also check that the link resolves to the correct file
  if diff /home/user/summary.txt "$link_path" >/dev/null; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
