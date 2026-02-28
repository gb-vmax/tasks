#!/bin/bash
result=1
grep -q "declare -x PROJECT=\"unix\"" /home/user/envlist.txt || result=0
grep -q "declare -x MODE=\"testing\"" /home/user/envlist.txt || result=0
echo $result > /logs/verifier/reward.txt
