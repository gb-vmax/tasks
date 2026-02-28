#!/bin/bash
set -e
if [ ! -f /home/user/traces/trace1.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
grep -q "127.0.0.1" /home/user/traces/trace1.txt && grep -qi "traceroute" /home/user/traces/trace1.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
