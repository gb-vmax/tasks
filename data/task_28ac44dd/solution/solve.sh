#!/bin/bash
set -e
cd /home/user

# Filter lines where duration >= 300ms
awk -F'duration=' '{split($2,a,"ms"); if(a[1]+0 >= 300) print}' db/postgresql.log > db/slow_queries.log

# Count how many slow queries were found
count=$(wc -l < db/slow_queries.log | tr -d ' ')

printf '%s\n' "Filtered ${count} slow queries into slow_queries.log" > db/filter_log.txt
