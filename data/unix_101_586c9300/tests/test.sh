#!/bin/bash
if [ ! -L /home/user/docs/latest.log ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
linkpath=$(readlink /home/user/docs/latest.log)
if [ "$linkpath" != "../logs/build.log" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(cat /home/user/docs/latest.log)" != "Build finished successfully." ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
