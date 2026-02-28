#!/bin/bash
if [ ! -f /home/user/ping_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q '1 packets transmitted' /home/user/ping_output.txt && grep -q '1 received' /home/user/ping_output.txt && grep -q '127.0.0.1' /home/user/ping_output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
