#!/bin/bash
if [ "$([ -f /home/user/data/info.log.bak ] && cat /home/user/data/info.log)" = $'ERROR: FAILED TO LOAD
WARNING: DEPRECATED API
INFO: PROCESS STARTED' ] \
   && [ "$(cat /home/user/data/info.log.bak)" = $'error: failed to load
warning: deprecated api
info: process started' ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
