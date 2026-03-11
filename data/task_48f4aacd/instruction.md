Hey, I need your help analyzing some server logs to put together a diagnostics report. We had an incident yesterday and I've collected three different log files from the server. I need you to analyze them in parallel and then combine everything into a single diagnostic summary file.

The three log files are:
- `/home/user/diagnostics/access.log` — nginx access log
- `/home/user/diagnostics/app.log` — application log
- `/home/user/diagnostics/syslog` — system log

Here's what I need you to extract from each one, then combine into a final report.

---

### From `access.log` (nginx combined log format):

1. **Total request count** — total number of log lines.
2. **HTTP status code breakdown** — count of requests per status code, sorted numerically by status code.
3. **Top 3 requested endpoints** — the most frequently requested URL paths (the 7th field, space-separated), with counts. Sort by count descending; break ties alphabetically by path.
4. **Bandwidth total** — sum of the response bytes field (the 10th field). Report in bytes.

---

### From `app.log` (each line format: `YYYY-MM-DD HH:MM:SS [LEVEL] message`):

1. **Count of each log level** — count lines by level (INFO, WARN, ERROR), sorted alphabetically by level name.
2. **All ERROR messages** — extract just the message portion (everything after `[ERROR] `) from ERROR lines, listed in the order they appear.
3. **First and last log timestamp** — the timestamp from the very first and very last line of the file.

---

### From `syslog` (standard syslog format: `Mon DD HH:MM:SS hostname process[pid]: message`):

1. **Count of unique processes** — how many distinct process names appear (the part before `[` in the 5th field; if no `[` then the whole 5th field, strip trailing `:`).
2. **Lines containing "error" or "Error" or "ERROR"** — count of such lines.
3. **Top 2 most frequent processes** by line count, sorted by count descending; break ties alphabetically.

---

### Final report

Combine all results into `/home/user/diagnostics/report.txt` with **exactly** this format (replace angle-bracket placeholders with actual values):

```
=== DIAGNOSTICS REPORT ===

--- ACCESS LOG ---
Total requests: <N>
Status codes:
  <code>: <count>
  <code>: <count>
  ...
Top endpoints:
  <path>: <count>
  <path>: <count>
  <path>: <count>
Total bandwidth: <N> bytes

--- APPLICATION LOG ---
Log levels:
  ERROR: <count>
  INFO: <count>
  WARN: <count>
Errors:
  - <message>
  - <message>
  ...
First log entry: <YYYY-MM-DD HH:MM:SS>
Last log entry: <YYYY-MM-DD HH:MM:SS>

--- SYSTEM LOG ---
Unique processes: <N>
Error-related lines: <N>
Top processes:
  <process>: <count>
  <process>: <count>
```

The file must end with a newline after the last line. There should be no trailing spaces on any line. The section separators (`---`) and headers must match exactly as shown.
