#!/bin/bash
expected='Name   Age  City
Alice  30   Boston
Bob    25   Seattle
Carol  22   Miami'
actual=$(cat /home/user/table.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
