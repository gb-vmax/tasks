#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/db_query_optim/old_links && [ -L /home/user/db_query_optim/active_query.sql ] && mv /home/user/db_query_optim/active_query.sql /home/user/db_query_optim/old_links/ || true && ln -sf /home/user/db_query_optim/query_prod.sql /home/user/db_query_optim/active_query_prod.sql && ln -sf /home/user/db_query_optim/query_test.sql /home/user/db_query_optim/active_query_test.sql && ln -sf /home/user/db_query_optim/query_dev.sql /home/user/db_query_optim/active_query_dev.sql && printf "active_query_prod.sql -> /home/user/db_query_optim/query_prod.sql\nactive_query_test.sql -> /home/user/db_query_optim/query_test.sql\nactive_query_dev.sql -> /home/user/db_query_optim/query_dev.sql\n" > /home/user/db_query_optim/symlink_report.txt
cat /home/user/db_query_optim/symlink_report.txt
