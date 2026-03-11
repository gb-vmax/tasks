I'm a system administrator and I have a server inventory CSV file at `/home/user/servers/inventory.csv`. I need to quickly generate a plain-text report that lists only the servers with status `active`, formatted in a specific way for our monitoring dashboard.

The CSV file has the following columns (with a header row):
```
hostname,ip_address,role,status,os
```

I need you to transform this file into a new file at `/home/user/servers/active_servers.txt`. The output file should:

1. Contain **no header line**.
2. Include **only rows where the status field is `active`**.
3. Each line should follow this exact format:
   ```
   [<hostname>] <ip_address> (<role>)
   ```
   For example, a row like `webserver01,10.0.1.5,web,active,Ubuntu` should become:
   ```
   [webserver01] 10.0.1.5 (web)
   ```
4. The lines should appear in the **same order** as they appear in the original CSV file.
5. The `os` column should be **omitted** entirely from the output.

Please create the output file `/home/user/servers/active_servers.txt` with the correctly transformed and filtered content.
