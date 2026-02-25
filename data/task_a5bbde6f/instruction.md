As an observability engineer, you have received a raw CSV export of service health checks from your monitoring system. You need to process and analyze this data for your dashboard tuning. Specifically, perform the following steps:

1. In the directory /home/user/obs-data/ you will find a file named service_health.csv. This file contains columns: service_name, status, response_time_ms, checked_at (ISO-8601 format).
2. Create a new CSV file at /home/user/obs-data/service_health_summary.csv with the following format:
   - Columns: service_name, total_checks, success_count, failure_count, avg_response_time_ms.
   - Each row should summarize each unique service_name:
     - total_checks: total number of rows for that service.
     - success_count: number of times status=="success".
     - failure_count: number of times status!="success".
     - avg_response_time_ms: average response_time_ms (rounded to two decimal places).
   - The output CSV should include a single header row and one row per service_name, sorted alphabetically by service_name.
3. Convert service_health_summary.csv into a JSON file at /home/user/obs-data/service_health_summary.json. The JSON file should be an array of objects, with each object containing these keys: service_name, total_checks, success_count, failure_count, avg_response_time_ms (a number, not a string).
4. Save a log file named /home/user/obs-data/dashboard_update.log. It should have the following format:
   - Each line: [YYYY-MM-DD HH:MM:SS] <action>: <details>
   - Actions to log: SUMMARY_CSV_CREATED (when service_health_summary.csv is created), SUMMARY_JSON_CREATED (when service_health_summary.json is created).
   - <details> should indicate the path of the file created.

When you finish, there should be three files in /home/user/obs-data/: service_health_summary.csv, service_health_summary.json, and dashboard_update.log, with contents and formats exactly as described above. The automated test will verify the contents and formatting of these files.
