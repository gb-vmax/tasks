Hey, I need your help filtering through a health check log file on my server. I'm a site reliability engineer and I need to quickly pull out all the failed uptime checks from today's monitoring log so I can send them to the on-call team.

The log file is at `/home/user/logs/uptime_monitor.log`. Each line follows this format:

```
[TIMESTAMP] [LEVEL] host=<hostname> status=<STATUS> response_time_ms=<N> check_id=<ID>
```

For example:
```
[2024-06-10T08:01:44Z] [INFO] host=api.example.com status=UP response_time_ms=142 check_id=chk_001
[2024-06-10T08:03:12Z] [ERROR] host=db.internal status=DOWN response_time_ms=5001 check_id=chk_002
```

I need you to extract only the lines where `status=DOWN` or `status=TIMEOUT` and write them to a new file at `/home/user/logs/failed_checks.txt`.

The output file should contain only the matching lines, exactly as they appear in the original log (no extra formatting, no added text, no headers). Each line should be preserved verbatim from the source file.

After that, I also need a quick count: write the total number of failed checks as a single integer on its own line to `/home/user/logs/failed_count.txt`. Nothing else in that file — just the number.

Can you do that for me?
</think>

<task>
Hey, I need your help filtering through a health check log file on my server. I'm a site reliability engineer and I need to quickly pull out all the failed uptime checks from today's monitoring log so I can send them to the on-call team.

The log file is at `/home/user/logs/uptime_monitor.log`. Each line follows this format:

```
[TIMESTAMP] [LEVEL] host=<hostname> status=<STATUS> response_time_ms=<N> check_id=<ID>
```

For example:
```
[2024-06-10T08:01:44Z] [INFO] host=api.example.com status=UP response_time_ms=142 check_id=chk_001
[2024-06-10T08:03:12Z] [ERROR] host=db.internal status=DOWN response_time_ms=5001 check_id=chk_002
```

I need you to extract only the lines where `status=DOWN` or `status=TIMEOUT` and write them to a new file at `/home/user/logs/failed_checks.txt`.

The output file should contain only the matching lines, exactly as they appear in the original log (no extra formatting, no added text, no headers). Each line should be preserved verbatim from the source file. The order of lines should match the order they appear in the original log file.

After that, I also need a quick count: write the total number of failed checks as a single integer on its own line to `/home/user/logs/failed_count.txt`. Nothing else in that file — just the number.

Can you do that for me?
