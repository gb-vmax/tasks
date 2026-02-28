#!/bin/bash
# Check that aliases.txt exists and contains the defined aliases
if [ ! -f /home/user/aliases.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
cnt=0
grep -q "alias ll='ls -l'" /home/user/aliases.txt && cnt=$((cnt+1))
grep -q "alias gs='git status'" /home/user/aliases.txt && cnt=$((cnt+1))
grep -q "alias la='ls -A'" /home/user/aliases.txt && cnt=$((cnt+1))
if [ $cnt -eq 3 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
