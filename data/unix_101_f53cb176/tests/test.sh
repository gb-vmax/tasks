#!/bin/bash
if [ ! -f /home/user/ping_summary.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Should NOT contain individual icmp_seq lines
grep -q 'packets transmitted' /home/user/ping_summary.txt && grep -q 'received' /home/user/ping_summary.txt && ! grep -q 'icmp_seq' /home/user/ping_summary.txt && [ "$(wc -l < /home/user/ping_summary.txt)" -le 5 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
