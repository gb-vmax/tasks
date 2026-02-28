#!/bin/bash
if [ -f /home/user/uname_all.txt ] && [ $(wc -l < /home/user/uname_all.txt) -eq 1 ] && grep -qE '^[^ ]+ [^ ]+ [^ ]+ .+' /home/user/uname_all.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
