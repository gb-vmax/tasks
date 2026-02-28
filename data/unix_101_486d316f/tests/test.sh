#!/bin/bash
set -e
out=/home/user/output.txt
if [ ! -f "$out" ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
# Should contain 2 file headers and each file's first 20 bytes
alpha_head="ABCDEFGHIJKLMNOPQRSTUVWXYZ\n1234567890abcdefghij\n"
beta_head="Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\n"
alpha_bytes=$(printf "%s" "$alpha_head" | head -c 20)
beta_bytes=$(printf "%s" "$beta_head" | head -c 20)
expected="==> /home/user/data/alpha.txt <==
$alpha_bytes
==> /home/user/data/beta.txt <==
$beta_bytes"
actual=$(cat "$out")
if [ "$expected" = "$actual" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
