#!/bin/bash
set -e
# Save output to a file for checking (simulate agent typing command)
ulimit -a > /home/user/ulimit_output.txt
# Check that the output contains several key resource limit labels (a subset, since exact values may vary)
grep -q "open files" /home/user/ulimit_output.txt && grep -q "core file size" /home/user/ulimit_output.txt && grep -q "max user processes" /home/user/ulimit_output.txt && grep -q "cpu time" /home/user/ulimit_output.txt && grep -q "max memory size" /home/user/ulimit_output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
