Hey, I need your help with a quick provisioning task. I have a server inventory file at `/home/user/infra/servers.csv` that lists all our servers. I need to extract just the hostnames of servers in the `prod` environment that are currently marked as `unprovisioned`, and write them into an Ansible-compatible inventory file.

The CSV file has a header row followed by data rows. Each row has these comma-separated columns in order: `hostname`, `ip_address`, `environment`, `status`, `role`.

I need you to generate a new file at `/home/user/infra/provision_targets.ini` that contains only the hostnames of servers where the `environment` column is exactly `prod` AND the `status` column is exactly `unprovisioned`.

The output file must look exactly like this:

```
[provision_targets]
<hostname1>
<hostname2>
...
```

So the first line is the literal text `[provision_targets]` and each subsequent line is one matching hostname, one per line, in the same order they appear in the CSV (top to bottom). There should be no blank lines, no trailing spaces, and no extra content.

Can you create that output file from the CSV?
