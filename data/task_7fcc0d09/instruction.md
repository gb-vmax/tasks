Hey, I need help analyzing my Nginx access log. I'm getting complaints from users about 404 errors on our API endpoints, and I want to quickly pull out just the relevant lines and summarize what's happening.

The log file is at `/home/user/logs/access.log`. It's in standard Nginx combined log format, which looks like this:

```
<ip> - - [<date>] "<method> <path> HTTP/1.1" <status> <bytes> "<referrer>" "<user-agent>"
```

I need you to do the following:

**Step 1:** Extract all lines where the HTTP status code is `404` AND the request path starts with `/api/`. Write those matching lines — unmodified, exactly as they appear in the log — to `/home/user/logs/api_404s.log`.

The status code appears as the 6th space-delimited field (after the closing quote of the request method+path). The path is inside the quoted request string (second field of that quoted portion). You should use a regex that correctly matches both conditions simultaneously. The lines should appear in the same order as they appear in the original log. Do not include any lines that are 404s for non-`/api/` paths, and do not include any lines that are errors on `/api/` paths with a status other than 404.

**Step 2:** Count how many unique IP addresses appear in the filtered results from `api_404s.log` (i.e., among the 404 `/api/` requests). The IP address is always the very first field on each line.

Write a summary file to `/home/user/logs/api_404_summary.txt` with **exactly** this format (no extra blank lines, no trailing spaces):

```
Total 404s on /api/: <N>
Unique IPs: <M>
```

Where `<N>` is the total number of matching log lines and `<M>` is the count of distinct IP addresses among those lines.
