#!/bin/bash
expected_paths="/home/user/data
/home/user/data/file1.txt
/home/user/data/alpha
/home/user/data/alpha/a.bin
/home/user/data/beta
/home/user/data/beta/b.txt"
# Run du to get sizes in bytes with total
du_output="$(du -ab --total /home/user/data 2>/dev/null)"
# Remove possible trailing whitespace
mapfile -t lines < <(echo "$du_output")
last_line="${lines[-1]}"
if [[ "$last_line" != total* ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that all expected paths appear in the output
all_found=1
while read -r path; do
  if ! grep -q "$path" <<< "$du_output"; then
    all_found=0
    break
  fi
done <<< "$expected_paths"
echo $all_found > /logs/verifier/reward.txt
