#!/bin/bash
set -e
[ ! -f "/home/user/data/file one.txt" ] &&
[ ! -f "/home/user/data/file two.txt" ] &&
[ -f "/home/user/data/important.txt" ] &&
[ -f "/home/user/data/keep.txt" ] &&
[ -d /home/user/data ] &&
echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
