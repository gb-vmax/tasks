#!/bin/bash
if [ -p /home/user/mypipe ] && [ ! -f /home/user/mypipe ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
