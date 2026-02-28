#!/bin/bash
set -e
cd /home/user
rm -rf extract_dir
mkdir extract_dir
cd extract_dir
cpio -idmv < ../archive.cpio >/dev/null 2>&1
if [[ -f file1.txt && -f file2.txt ]]; then
  diff file1.txt ../file1.txt >/dev/null && diff file2.txt ../file2.txt >/dev/null && echo 1 > /logs/verifier/reward.txt && exit 0
fi
echo 0 > /logs/verifier/reward.txt
