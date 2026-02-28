#!/bin/bash
if grep -q 'No such file or directory' /logs/verifier/stderr.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
