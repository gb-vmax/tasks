#!/bin/bash
awk '{sum += $2} END {print sum}' /home/user/numbers.txt > /home/user/col2_sum.txt
