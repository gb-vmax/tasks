#!/bin/bash
set -e
cd /home/user

cat /home/user/sql-optimizer/VERSION
echo -n "1.5.0" > /home/user/sql-optimizer/VERSION
head -20 /home/user/sql-optimizer/CHANGELOG.md
(echo -e "## [1.5.0] - 2024-06-05\n- Optimized SELECT queries for faster execution.\n"; cat /home/user/sql-optimizer/CHANGELOG.md) > /home/user/sql-optimizer/CHANGELOG.md.tmp && mv /home/user/sql-optimizer/CHANGELOG.md.tmp /home/user/sql-optimizer/CHANGELOG.md
cat /home/user/sql-optimizer/VERSION && echo && cat /home/user/sql-optimizer/CHANGELOG.md
