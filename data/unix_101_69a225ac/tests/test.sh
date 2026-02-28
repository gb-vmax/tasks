#!/bin/bash
set -e
# Check that archive exists and contains both files
cd /home/user
tmpdir=$(mktemp -d)
cp backup.cpio "$tmpdir/"
cd "$tmpdir"
cpio -t < backup.cpio > contents.txt
cd /home/user
if grep -q "/home/user/report.txt" "$tmpdir/contents.txt" && grep -q "/home/user/data.csv" "$tmpdir/contents.txt"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
