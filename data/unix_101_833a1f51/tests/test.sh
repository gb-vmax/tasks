#!/bin/bash
if [[ $(cat /home/user/output.txt) == 'Hello Unix' ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
