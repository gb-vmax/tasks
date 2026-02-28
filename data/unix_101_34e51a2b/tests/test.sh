#!/bin/bash
if [ ! -f /home/user/numbered.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'     1	First line\n     2\t\n     3\tSecond line\n     4\tThird line'
actual=$(cat /home/user/numbered.txt | sed 's/ *$//')
if [ "$actual" = "     1	First line
     2	
     3	Second line
     4	Third line" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
