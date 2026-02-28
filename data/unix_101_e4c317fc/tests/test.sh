#!/bin/bash
set -e
if [ ! -f /home/user/first5.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
count=$(wc -l < /home/user/first5.txt)
if [ "$count" -ne 5 ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
expected="The woods are lovely, dark and deep
But I have promises to keep
And miles to go before I sleep
And miles to go before I sleep
Whose woods these are I think I know."
actual=$(cat /home/user/first5.txt)
if [ "$expected" = "$actual" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
