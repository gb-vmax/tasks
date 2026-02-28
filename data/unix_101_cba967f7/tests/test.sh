#!/bin/bash
expected='<<<<<<< /home/user/theirs.txt
World!
=======
World
Goodbye
>>>>>>> /home/user/yours.txt'
if grep -Fq "<<<<<<< /home/user/theirs.txt" /home/user/merge.diff3 && grep -Fq 'World!' /home/user/merge.diff3 && grep -Fq 'World' /home/user/merge.diff3 && grep -Fq 'Goodbye' /home/user/merge.diff3 && grep -Fq '>>>>>>> /home/user/yours.txt' /home/user/merge.diff3; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
