I'm a compliance officer and I need your help processing a system access audit log. We received a tab-separated file at `/home/user/audit/access_log.tsv` that contains columns in this order:

```
timestamp	username	ip_address	system	action	status
```

For our compliance report, I need to produce a new file at `/home/user/audit/compliance_report.tsv` that contains **only the following columns, in this exact order**:

```
username	system	action	timestamp
```

The output file must:
- Be tab-separated (same as the input)
- Include the header row (reordered accordingly)
- Include all data rows, reordered in the same way
- Not include the `ip_address` or `status` columns at all

After that, I also need a second file at `/home/user/audit/usernames.txt` that contains **only the unique usernames** (no header, just the data values) from the original log, one per line, sorted alphabetically.

Please produce both output files from the source data.
