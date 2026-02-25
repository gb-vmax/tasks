You are a performance engineer profiling several applications and need to analyze memory usage. In the directory /home/user/profile_data, you will find a file named app_memory.csv. It contains three columns: application (string), timestamp (ISO 8601 datetime), and rss_MB (integer, resident set size in megabytes). 

Your tasks are as follows:

1. For each application, calculate the highest recorded rss_MB value.
2. Save these results in a new JSON file at /home/user/profile_data/max_memory_per_app.json. The file should be a single JSON object, where each key is the application name, and each value is the maximum rss_MB value (integer) for that application.

For example, if the CSV had this data:
```
application,timestamp,rss_MB
auth_service,2024-03-08T10:00:00,132
data_collector,2024-03-08T10:00:00,240
auth_service,2024-03-08T10:05:00,235
```
The JSON should look like:
```json
{
  "auth_service": 235,
  "data_collector": 240
}
```

Be sure your output file is properly formatted JSON (with keys as strings and integer values), and contains only the maximum rss_MB per application present in the CSV. No extra data or arrays should appear in the output.
