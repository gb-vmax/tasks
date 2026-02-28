#!/bin/bash
if [ ! -f /home/user/logpart_000 ] || [ ! -f /home/user/logpart_001 ] || [ ! -f /home/user/logpart_002 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
file0=$(cat /home/user/logpart_000)
file1=$(cat /home/user/logpart_001)
file2=$(cat /home/user/logpart_002)
if [ "$file0" = $'INFO Startup complete\nINFO User login\n' ] && [ "$file1" = $'INFO Retry\n' ] && [ "$file2" = $'INFO Shutdown\n' ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
