#!/bin/bash
if [[ -f /home/user/targetdir/source1.txt ]] && grep -qxF 'Hello World' /home/user/targetdir/source1.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
