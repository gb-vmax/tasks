#!/bin/bash
if [ ! -f /home/user/archive.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ ! -f /home/user/data.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(stat -c '%i' /home/user/data.txt)" != "$(stat -c '%i' /home/user/archive.txt)" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(cat /home/user/archive.txt)" != "Project Data 2024" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
