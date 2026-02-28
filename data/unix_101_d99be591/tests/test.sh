#!/bin/bash
if [ ! -f /home/user/whoami_help.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'Print the user name associated' /home/user/whoami_help.txt && grep -q 'Usage: whoami' /home/user/whoami_help.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
