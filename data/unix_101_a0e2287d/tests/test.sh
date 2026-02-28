#!/bin/bash
if [ ! -f /home/user/name.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -qx 'Alice' /home/user/name.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
