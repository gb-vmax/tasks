#!/bin/bash
if [ ! -f /home/user/output.hex ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'Hello, world!' /home/user/output.hex; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
