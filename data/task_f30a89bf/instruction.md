I'm a compliance officer doing an audit and I need your help processing a system access log. We have a tab-separated file at `/home/user/audit/access_log.tsv` that contains records of user logins across our servers. The file has the following columns in this order:

1. `timestamp`
2. `username`
3. `server_id`
4. `ip_address`
5. `access_level`
6. `session_duration_mins`

I only need columns 1, 2, 3, and 5 for my compliance report — I don't need IP addresses or session durations. I also need them in a different column order: `username`, `server_id`, `access_level`, `timestamp` (in that exact order, tab-separated).

Please produce the output file at `/home/user/audit/compliance_report.tsv`. The file should include a header line as the first row and then all the data rows. The header should read exactly:

```
username	server_id	access_level	timestamp
```

Do not include the original header from the source file in the output — replace it entirely with the new header. All fields must remain tab-separated in the output. The file should end with a newline after the last data row.
