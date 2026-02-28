#!/bin/bash
set -e
cd /home/user
if [ ! -f docs.zip ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
unzip -l docs.zip | grep -q 'docs/a.txt' && unzip -l docs.zip | grep -q 'docs/b.txt' && ! unzip -l docs.zip | grep -q 'subdir/c.txt' && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
