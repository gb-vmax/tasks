#!/bin/bash
PASS=1
# Test that combined_reversed.txt exists and has the correct reversed lines
if [ ! -f /home/user/combined_reversed.txt ]; then PASS=0; fi
EXPECTED_COMBINED='ahpla
ateb
ammag
atled'
ACTUAL_COMBINED=$(cat /home/user/combined_reversed.txt | tr -d '\r')
if [ "$ACTUAL_COMBINED" != "$EXPECTED_COMBINED" ]; then PASS=0; fi
# Test that rev_help.txt contains usage information
if ! grep -q "Reverse lines characterwise" /home/user/rev_help.txt; then PASS=0; fi
echo $PASS > /logs/verifier/reward.txt
