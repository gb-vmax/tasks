#!/bin/bash
out=$(zgrep 'ERROR' /home/user/logs/app.log.gz)
if [[ "$out" == "ERROR Failed to start
ERROR Timeout" ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
