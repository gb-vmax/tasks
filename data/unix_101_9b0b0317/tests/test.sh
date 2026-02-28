#!/bin/bash
expected=$'started\nsinging\ndanced\njumped\nrunning\nplayed'
actual=$(egrep -o '\b\w+(ing|ed)\b' /home/user/texts/first.txt /home/user/texts/second.txt | sort | uniq)
if [ "$actual" == "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
