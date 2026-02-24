#!/bin/bash
# Ground truth reference (not an executable solution):
#
# - There is no file at /home/user/resource_usage.db before task execution.
# - After step 1, /home/user/resource_usage.db is created and contains a table named usage_stats with columns:
#     - server_name (type: TEXT)
#     - cpu_percent (type: REAL)
#     - memory_mb (type: INTEGER)
#     - timestamp (type: TEXT)
# - The table usage_stats contains exactly the following three rows (exact order does not matter):
#     - ('Alpha01', 43.0, 6084, '2024-04-30T11:58:00Z')
#     - ('Beta02', 85.2, 9560, '2024-04-30T11:58:00Z')
#     - ('Gamma03', 22.7, 4032, '2024-04-30T11:58:00Z')
# - The summary query: 
#     SELECT avg(cpu_percent) as avg_cpu_percent, max(memory_mb) as max_memory_mb FROM usage_stats;
#   Should produce:
#     avg_cpu_percent|max_memory_mb
#     50.3|9560
# - The file /home/user/usage_summary.txt exists and contains (with no trailing newline or extra whitespace, and without header):
#     50.3|9560

echo 'No automated solution provided.'
