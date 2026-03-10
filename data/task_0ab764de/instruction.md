I'm a log analyst investigating slow API requests on our web server. I have an access log file at `/home/user/logs/access.log`. Each line follows this format:

```
<timestamp> <client_ip> <method> <endpoint> <status_code> <response_time_ms>
```

For example:
```
2024-06-01T08:12:03Z 192.168.1.10 GET /api/users 200 143
2024-06-01T08:13:45Z 10.0.0.5 POST /api/orders 500 892
```

I need you to extract all requests where the response time exceeds 400 milliseconds, and write a reformatted summary to `/home/user/logs/slow_requests.txt`.

Each matching line should be transformed into this exact format:
```
[<timestamp>] <method> <endpoint> => <response_time_ms>ms (<status_code>)
```

For example, the line:
```
2024-06-01T08:13:45Z 10.0.0.5 POST /api/orders 500 892
```
would become:
```
[2024-06-01T08:13:45Z] POST /api/orders => 892ms (500)
```

The output file should contain only the matching (reformatted) lines, one per line, in the same order they appear in the original log. There should be no blank lines, no header, and no trailing whitespace on any line.

Please process `/home/user/logs/access.log` and write the results to `/home/user/logs/slow_requests.txt`.
