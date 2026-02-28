#!/bin/bash
if [ ! -f /home/user/sorted.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# The input graph:
# E -> D -> C <- B <- A
# So one valid topological sort is: E D A B C
# But tsort may output D E A B C or other valid orderings, as long as dependencies are respected.
# So let's check that in sorted.txt, for every dependency X Y in order.txt, X appears before Y.
mapfile -t sorted < /home/user/sorted.txt
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
done < /home/user/order.txt
echo $pass > /logs/verifier/reward.txt
