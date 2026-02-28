#!/bin/bash
awk -F '\t' 'NR>1 {sum += $3} END {print sum}' /home/user/sales.tsv > /home/user/total_sales.txt
