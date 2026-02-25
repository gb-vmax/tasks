#!/bin/bash
set -e
cd /home/user

grep -E 'duration:(2[0-9][1-9]|[3-9][0-9][0-9]|[1-9][0-9]{3,})ms' /home/user/db/query.log > /home/user/db/slow_queries.log
cat /home/user/db/slow_queries.log
