#!/bin/bash
set -e
cmp /home/user/file1.txt /home/user/file2.txt > /tmp/cmp_test.out 2>&1 && [ ! -s /tmp/cmp_test.out ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
