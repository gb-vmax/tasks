#!/bin/bash
set -e
cd /home/user

echo "Total SUCCESS: $(grep -c 'SUCCESS$' /home/user/migration/migration.log)
Total FAILURE: $(grep -c 'FAILURE$' /home/user/migration/migration.log)" > /home/user/migration/migration_summary.txt
cat /home/user/migration/migration_summary.txt
