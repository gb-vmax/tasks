#!/bin/bash
if [ ! -f /home/user/decoded.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if cmp -s /home/user/decoded.txt /home/user/raw.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
