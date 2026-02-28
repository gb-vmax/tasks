#!/bin/bash
set -e
if [ ! -f /home/user/article_wrapped.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
maxlen=$(awk '{if(length>m) m=length} END{print m}' /home/user/article_wrapped.txt)
if [ "$maxlen" -le 15 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
