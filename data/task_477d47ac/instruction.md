I'm a log analyst and I need your help investigating error patterns in our application logs. There's a log file at `/home/user/logs/app.log` that I need to analyze.

Please do the following:

1. Search through `/home/user/logs/app.log` for all lines containing the word `ERROR` and save only those lines into a new file at `/home/user/logs/errors_only.log`. The file should contain just the matching lines, one per line, in the same order they appear in the original log.

2. Count the number of lines in `/home/user/logs/errors_only.log` and write a summary file at `/home/user/logs/error_summary.txt` with exactly this content (replacing `<N>` with the actual count):

```
Total ERROR lines: <N>
```

The file should contain exactly one line with no trailing blank lines. The automated test will check the exact contents of both output files, so please make sure the formatting matches precisely.
