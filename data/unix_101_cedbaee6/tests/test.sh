#!/bin/bash
if [ ! -f /home/user/libalpha.a ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
ar t /home/user/libalpha.a > /tmp/arlist.txt
if grep -Fxq "alpha.o" /tmp/arlist.txt && grep -Fxq "beta.o" /tmp/arlist.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
