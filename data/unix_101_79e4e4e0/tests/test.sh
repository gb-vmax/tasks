#!/bin/bash
if [ ! -d /home/user/app/bin/logs ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ ! -d /home/user/app/bin ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ ! -d /home/user/app ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
