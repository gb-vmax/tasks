Hey, I need your help fixing up our observability dashboard configuration. We have a dashboard registry file at `/home/user/observability/dashboards.json` that lists all our monitoring panels. Some of them are broken — they have `"status": "error"` or they're missing a `"threshold"` field entirely (the key is absent from the panel object).

I need you to scan through that file and produce a repair report at `/home/user/observability/repair_report.txt`.

The file contains a top-level JSON object with a `"dashboards"` array. Each dashboard object has these fields:
- `"name"`: string — the dashboard name
- `"status"`: string — either `"ok"` or `"error"`
- `"threshold"`: integer — may be missing entirely on some entries

I want the repair report to list every dashboard that needs attention — meaning any dashboard where `status` is `"error"` OR where the `"threshold"` key is completely absent. Each such dashboard should appear as one line in this exact format:

```
[NEEDS REPAIR] <name> | status=<status> | threshold=<threshold_value_or_MISSING>
```

Where:
- `<name>` is the dashboard's name field
- `<status>` is either `ok` or `error`
- `<threshold_value_or_MISSING>` is the numeric threshold value if the key exists, or the literal word `MISSING` if the key is absent

After all the dashboard lines, append a blank line followed by this summary line:

```
Total dashboards needing repair: <N>
```

The entries in the report should appear in the same order they appear in the `dashboards.json` file.

Do not include dashboards that have `"status": "ok"` AND have a `"threshold"` key present — those are fine.

Can you generate that report for me?
