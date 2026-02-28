#!/bin/bash
if [ ! -f /home/user/out.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# The input:
# liba -> libc -> libd
# libb -> libc
# libe -> libd
# libf -> libe
# So a valid sort: liba, libb, libc, libf, libe, libd
# Let's check that for every dependency X Y, X appears before Y.
mapfile -t sorted < /home/user/out.txt
get_index() {
  local val="$1"
  for i in "${!sorted[@]}"; do
    if [ "${sorted[$i]}" = "$val" ]; then
      echo $i
      return 0
    fi
  done
  echo -1
}
pass=1
while read -r from to; do
  idx_from=$(get_index "$from")
  idx_to=$(get_index "$to")
  if [ "$idx_from" -eq -1 ] || [ "$idx_to" -eq -1 ] || [ "$idx_from" -ge "$idx_to" ]; then
    pass=0
    break
  fi
done < /home/user/input.txt
echo $pass > /logs/verifier/reward.txt
