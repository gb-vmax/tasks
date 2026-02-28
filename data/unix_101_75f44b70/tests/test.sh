#!/bin/bash
if [ -p /home/user/pipes/securepipe ] && [ "$(stat -c%a /home/user/pipes/securepipe)" = "600" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
