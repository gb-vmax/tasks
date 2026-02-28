#!/bin/bash
EXPECTED=$'file1\t1.0K\tinfoA\nfile2\t2.0K\tinfoB\nfile3\t1.0M\tinfoC'
RESULT=$(cat /home/user/data/report.tsv)
if [[ "$RESULT" == "$EXPECTED" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
