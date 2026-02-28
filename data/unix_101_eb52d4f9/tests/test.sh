#!/bin/bash
if [ ! -f /home/user/limited_copy.bin ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if cmp -s /home/user/bigfile.bin /home/user/limited_copy.bin; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
