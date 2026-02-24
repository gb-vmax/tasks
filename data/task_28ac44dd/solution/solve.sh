#!/bin/bash
# Ground truth reference (not an executable solution):
#
# The file /home/user/db/postgresql.log exists before the task starts. Its contents are:
# 
# [2024-05-22 14:23:11] user=alice db=inventory duration=145ms statement: SELECT * FROM products;
# [2024-05-22 14:25:42] user=bob db=sales duration=384ms statement: UPDATE orders SET status='shipped' WHERE id=1492;
# [2024-05-22 14:26:00] user=carol db=inventory duration=92ms statement: DELETE FROM products WHERE id=3482;
# [2024-05-22 14:27:03] user=dan db=inventory duration=518ms statement: INSERT INTO products VALUES (1023, 'pen', 1.20);
# [2024-05-22 14:30:14] user=alice db=sales duration=215ms statement: SELECT * FROM orders WHERE status='shipped';
# [2024-05-22 14:31:22] user=dan db=inventory duration=301ms statement: SELECT COUNT(*) FROM products;
# [2024-05-22 14:32:45] user=bob db=sales duration=44ms statement: SELECT * FROM customers;
# 
# After task completion, the file /home/user/db/slow_queries.log must contain (order preserved):
# 
# [2024-05-22 14:25:42] user=bob db=sales duration=384ms statement: UPDATE orders SET status='shipped' WHERE id=1492;
# [2024-05-22 14:27:03] user=dan db=inventory duration=518ms statement: INSERT INTO products VALUES (1023, 'pen', 1.20);
# [2024-05-22 14:31:22] user=dan db=inventory duration=301ms statement: SELECT COUNT(*) FROM products;
# 
# The file /home/user/db/filter_log.txt must exist and contain exactly:
# 
# Filtered 3 slow queries into slow_queries.log
# 
# No other files should be created or modified.

echo 'No automated solution provided.'
