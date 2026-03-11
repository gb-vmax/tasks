Hey, I'm building an automation workflow and I need your help processing some data. I have a JSON file at `/home/user/data/services.json` that contains a list of monitoring services. I need to convert specific fields from this JSON into a CSV file that our alerting system can ingest.

The JSON file contains an array of service objects. Each object has these fields: `id`, `name`, `status`, `region`, `response_time_ms`, and `owner_email`.

Please extract only the `id`, `name`, `status`, and `response_time_ms` fields from each service object and write them as a CSV file to `/home/user/data/services_report.csv`.

The CSV must:
- Have a header row exactly: `id,name,status,response_time_ms`
- Have one row per service, in the same order they appear in the JSON file
- Use no extra spaces around commas or values
- Not have a trailing newline after the last data row

For example, if the JSON contained a service with id `42`, name `auth-service`, status `degraded`, and response_time_ms `320`, the corresponding CSV row would be:
```
42,auth-service,degraded,320
```

Please write the output to `/home/user/data/services_report.csv`.
