#!/bin/bash
set -e
cd /home/user

sqlite3 /home/user/capacity_resources.db "CREATE TABLE IF NOT EXISTS resources (id INTEGER PRIMARY KEY AUTOINCREMENT, resource_type TEXT, resource_name TEXT, usage_percent REAL CHECK(usage_percent >= 0 AND usage_percent <= 100), analysis_date TEXT);"
sqlite3 /home/user/capacity_resources.db "INSERT INTO resources (resource_type, resource_name, usage_percent, analysis_date) VALUES ('CPU', 'Server01', 63.5, '2024-06-01'); INSERT INTO resources (resource_type, resource_name, usage_percent, analysis_date) VALUES ('Memory', 'Server01', 74.2, '2024-06-01'); INSERT INTO resources (resource_type, resource_name, usage_percent, analysis_date) VALUES ('Disk', 'DBStorage', 87.9, '2024-06-01'); INSERT INTO resources (resource_type, resource_name, usage_percent, analysis_date) VALUES ('CPU', 'Server02', 41.0, '2024-06-01');"
sqlite3 -noheader -separator " " /home/user/capacity_resources.db "SELECT resource_type, ROUND(AVG(usage_percent),2), ROUND(MAX(usage_percent),2) FROM resources WHERE analysis_date = '2024-06-01' GROUP BY resource_type;" > /home/user/resource_stats.log
cat /home/user/resource_stats.log
