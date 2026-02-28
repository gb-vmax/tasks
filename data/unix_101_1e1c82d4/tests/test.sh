#!/bin/bash
set -e
if [ ! -f /home/user/file1.md5sum ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected_sum=$(md5sum /home/user/file1.txt | awk '{print $1}')
output_sum=$(awk '{print $1}' /home/user/file1.md5sum)
output_file=$(awk '{print $2}' /home/user/file1.md5sum)
if [ "$expected_sum" = "$output_sum" ] && [[ "$output_file" =~ file1.txt$ ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
