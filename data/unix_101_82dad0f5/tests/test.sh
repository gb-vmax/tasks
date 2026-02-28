#!/bin/bash
arp -a | grep -E '192\.168\.1\.20|00:11:22:33:44:55' >/dev/null 2>&1 && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
