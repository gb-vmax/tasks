I'm a sysadmin and I need your help processing a server inventory file. I have a JSON file at `/home/user/servers/inventory.json` that contains an array of server records. I need to extract specific fields from it and produce a clean CSV report.

The JSON file contains records with these fields: `hostname`, `ip_address`, `os`, `cpu_cores`, `ram_gb`, `status`, and `datacenter`.

Please convert this data into a CSV file at `/home/user/servers/report.csv` with the following requirements:

1. Include only these columns (in this exact order): `hostname`, `ip_address`, `cpu_cores`, `ram_gb`, `status`
2. The first line must be the header row: `hostname,ip_address,cpu_cores,ram_gb,status`
3. Sort the rows alphabetically by `hostname` (ascending)
4. No trailing spaces, no quoted fields — plain comma-separated values

For example, if a server has hostname `web01`, ip `10.0.0.1`, cpu_cores `4`, ram_gb `16`, status `active`, it should appear as:
```
web01,10.0.0.1,4,16,active
```

The final file should have one header line followed by one line per server, with a newline at the end of the file. Nothing else — no blank lines, no extra columns.
