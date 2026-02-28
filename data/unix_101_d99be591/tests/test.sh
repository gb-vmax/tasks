#!/bin/bash
if grep -q -i '^whoami (GNU coreutils)' /home/user/whoami_version.txt && grep -q 'Copyright' /home/user/whoami_version.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
