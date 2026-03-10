I'm building an ETL pipeline and I need your help quickly triaging some failures from last night's run. I have a log file at `/home/user/etl/pipeline.log` that contains mixed-severity log lines from several pipeline stages. I need to extract only the lines that represent actual data transformation errors so I can pass them to a downstream alerting script.

Specifically, I need you to filter the log file and write the results to `/home/user/etl/errors.log`. Here are the exact rules:

**Lines to extract:** Only lines where the severity token is `ERROR` AND the stage name (the bracketed word right after the severity) is either `[TRANSFORM]` or `[LOAD]`. Lines from `[EXTRACT]`, `[VALIDATE]`, or any other stage should be excluded — even if they are `ERROR` level. `WARN`, `INFO`, and `DEBUG` lines should never appear in the output regardless of stage.

The log lines follow this format:
```
YYYY-MM-DD HH:MM:SS | SEVERITY | [STAGE] | message text
```

For example, a matching line looks like:
```
2024-11-01 03:12:45 | ERROR | [TRANSFORM] | null value in non-nullable column "user_id"
2024-11-01 03:14:02 | ERROR | [LOAD] | deadlock detected on table "events", retrying
```

While these should NOT appear in the output:
```
2024-11-01 03:10:01 | ERROR | [EXTRACT] | connection timeout on source DB
2024-11-01 03:11:30 | WARN  | [TRANSFORM] | column "email" has 12% null rate
2024-11-01 03:13:15 | INFO  | [LOAD] | batch 4 of 9 committed successfully
```

After filtering, I also need the total count of matched lines written to `/home/user/etl/error_count.txt` as a plain integer with no extra text or whitespace — just the number followed by a newline.

Please make sure `errors.log` contains the matched lines in the same order they appear in `pipeline.log`, with no trailing blank lines and no modification to the line content.
