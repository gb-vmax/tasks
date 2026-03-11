Hey, I need some help debugging a service that's been acting up. I have an application log file at `/home/user/logs/service.log` that contains entries from multiple log levels (INFO, WARN, ERROR). Each line follows this format:

```
[LEVEL] YYYY-MM-DD HH:MM:SS - Message text here
```

I need you to do two things:

**1. Count how many ERROR-level lines are in the log file and write that count to `/home/user/logs/error_count.txt`.**

The file should contain exactly one line with just the integer count, like:
```
7
```
No trailing text, no label — just the number followed by a newline.

**2. Extract all ERROR-level lines from the log file and write them to `/home/user/logs/errors_only.log`.**

The output file should contain only the lines that begin with `[ERROR]`, preserving them exactly as they appear in the source file (same order, no modifications). Nothing else — no headers, no blank lines added, just the raw matching lines.

The log file already exists at `/home/user/logs/service.log`. You don't need to create the `logs` directory. Just produce the two output files.
