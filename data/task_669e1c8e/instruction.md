I'm a database administrator reviewing our application's configuration file to optimize slow queries. I need to extract specific connection and performance settings from our database INI config so I can compile them into a quick-reference summary file.

The database configuration file is located at `/home/user/db_config.ini`. It's a standard INI file with multiple sections. I need you to extract specific values from it and write them to a new file at `/home/user/db_summary.txt`.

The summary file must contain exactly the following key-value pairs, each on its own line, in this exact order:

```
host=<value of host from [connection] section>
port=<value of port from [connection] section>
max_connections=<value of max_connections from [performance] section>
query_timeout=<value of query_timeout from [performance] section>
slow_query_log=<value of slow_query_log from [logging] section>
```

Each line must use the format `key=value` with no spaces around the `=` sign, no trailing spaces, and no blank lines. The file should contain exactly 5 lines.

For example, if the `[connection]` section had `host = db.internal.example.com`, the corresponding line in the output file would be:
```
host=db.internal.example.com
```

Note that the INI file uses spaces around the `=` sign (e.g., `host = db.internal.example.com`), but the output file must NOT have spaces around the `=` sign.

Please create `/home/user/db_summary.txt` with exactly this content based on the values in `/home/user/db_config.ini`.
