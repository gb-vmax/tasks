#!/bin/bash
set -e
cd /home/user

ln -sf /home/user/database/logs/query.log /home/user/latest_queries.log && ls -l /home/user/latest_queries.log > /home/user/symlink_creation_output.txt
