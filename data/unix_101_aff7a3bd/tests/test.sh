#!/bin/bash
EXPECTED1="/home/user/bin/mycmd"
EXPECTED2="/usr/local/bin/mycmd"
mapfile -t lines < /home/user/mycmd_paths.txt
if [ "${lines[0]}" = "$EXPECTED1" ] && [ "${lines[1]}" = "$EXPECTED2" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
