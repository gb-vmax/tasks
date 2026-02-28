#!/bin/bash
if [ ! -f /home/user/fruits_updated.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'apple' /home/user/fruits_updated.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'orange' /home/user/fruits_updated.txt && grep -q 'orange pie' /home/user/fruits_updated.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
