Hey, I need help triaging some incidents from our monitoring system. I've got a JSON file at `/home/user/incidents/raw_incidents.json` that contains an array of incident objects. I need you to extract all **critical or high severity** incidents that are currently **open** (not resolved), and write them to a CSV file for the on-call team.

Each incident object in the JSON has these fields:
- `id`: string, e.g. "INC-001"
- `title`: string, a short description
- `severity`: string, one of "critical", "high", "medium", "low"
- `status`: string, one of "open", "resolved", "investigating"
- `service`: string, the affected service name
- `opened_at`: string, ISO 8601 timestamp e.g. "2024-11-01T08:23:00Z"

Please write the filtered and sorted results to `/home/user/incidents/triage.csv`.

The CSV must have exactly this header line:
```
id,severity,service,title,opened_at
```

Include only rows where `severity` is `"critical"` or `"high"` AND `status` is `"open"` OR `"investigating"` (i.e. exclude any incident that is fully `"resolved"`). So include open + investigating incidents with critical or high severity.

Sort the output rows by severity first (all `critical` rows before all `high` rows), then within the same severity sort by `opened_at` ascending (oldest first).

Each row should have exactly those five fields in that column order. If the `title` field contains a comma, it must be wrapped in double quotes.

The file should have no trailing newline after the last data row — just a final newline character ending that last row (standard Unix line endings).

Do not include any incidents with `severity` of `"medium"` or `"low"`, and do not include any incidents where `status` is `"resolved"`.
