#!/bin/bash
if [ -f /home/user/info.log.gz ] && [ -f /home/user/info.log.unzipped ] && grep -q "beta" /home/user/info.log.unzipped; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
