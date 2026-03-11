Hey, I need help debugging a service that's been acting up. I have an nginx-style service log file at `/home/user/logs/nginx-service.log` and I need to extract just the error lines and write them to a separate file, then also write a one-line summary.

The log file has entries in this format:
```
2024-05-10T08:12:01 [INFO] Service started successfully
2024-05-10T08:13:45 [ERROR] Failed to bind to port 8080: address already in use
2024-05-10T08:14:02 [WARNING] Retrying connection to upstream
...
```

Each line starts with a timestamp, then a log level in brackets (`[INFO]`, `[WARNING]`, `[ERROR]`), then the message.

Here's what I need you to do:

1. Extract all lines that contain `[ERROR]` from `/home/user/logs/nginx-service.log` and write them (preserving the original full line content, in the original order) to `/home/user/logs/errors_only.log`. The file should contain only the error lines, one per line, with no trailing blank line.

2. Count the total number of `[ERROR]` lines and write a summary line to `/home/user/logs/error_summary.txt`. The file should contain exactly one line in this format:
```
Total errors: <N>
```
Where `<N>` is the count of error lines. No trailing newline quirks — just the one line followed by a standard newline.

Please make sure the output files are created exactly as described — I have an automated check that will validate the contents.
