Hi, I'm a support engineer and I need to collect a quick diagnostics summary from a customer's application config file. The config file is at `/home/user/app/config.ini` and I need you to extract specific values from it and write a formatted diagnostics report.

Please parse `/home/user/app/config.ini` and create a file at `/home/user/diagnostics/report.txt` with exactly the following format:

```
=== DIAGNOSTICS REPORT ===
Host: <value of "host" key in the [database] section>
Port: <value of "port" key in the [database] section>
Log Level: <value of "level" key in the [logging] section>
Log File: <value of "file" key in the [logging] section>
Max Workers: <value of "max_workers" key in the [server] section>
Debug Mode: <value of "debug" key in the [server] section>
```

A few important notes about the format:
- The output file should have exactly 7 lines (one header line and six data lines).
- There should be no trailing spaces on any line.
- Each data line has the label, a colon, a single space, then the value — for example `Host: localhost`.
- The values should be taken exactly as they appear in the INI file (no quotes, no extra whitespace).
- The `/home/user/diagnostics/` directory may not exist yet — you'll need to create it.

The INI file uses standard format with section headers like `[database]` and key-value pairs separated by ` = ` (space-equals-space).
