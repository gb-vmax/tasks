#!/bin/bash
sleep 2
if [ -f /home/user/results/task2.out ] && grep -Fxq 'Processing' /home/user/results/task2.out && grep -Fxq 'Completed' /home/user/results/task2.out && [ "$(head -n1 /home/user/results/task2.out)" = "Processing" ] && [ "$(tail -n1 /home/user/results/task2.out)" = "Completed" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
