#!/bin/bash
if [ ! -f /home/user/people_table.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# There should be a header and 4 data rows
rows=$(wc -l < /home/user/people_table.txt)
[ "$rows" -eq 5 ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# The header should be aligned with data columns
header="$(head -n1 /home/user/people_table.txt)"
second_line="$(sed -n 2p /home/user/people_table.txt)"
# Columns should be separated by 2+ spaces (due to tabular formatting)
if [[ "$header" =~ [A-Za-z]+[[:space:]]{2,}[A-Za-z]+[[:space:]]{2,}[A-Za-z]+ ]] && [[ "$second_line" =~ [A-Za-z]+[[:space:]]{2,}[0-9]+[[:space:]]{2,}[A-Za-z]+ ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
