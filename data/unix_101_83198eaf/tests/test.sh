#!/bin/bash
if [ ! -f /home/user/nodigits.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q '[0-9]' /home/user/nodigits.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q '^abcdef$' /home/user/nodigits.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
