#!/bin/bash
if [ "$(cat /home/user/out.txt)" = "training" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
