#!/bin/bash
if [ ! -f /home/user/encoded.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
encoded=$(base64 /home/user/input.txt)
file_content=$(cat /home/user/encoded.txt)
if [ "$encoded" = "$file_content" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
