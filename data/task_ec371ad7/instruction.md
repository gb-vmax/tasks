I'm reorganizing my Python project and I need help extracting some information from our deployment configuration file. The project config is at `/home/user/project/deploy.ini`.

I need you to parse that INI file and create a summary file at `/home/user/project/config_summary.txt`. The summary should list the `host` and `port` values from every section in the INI file (in the order the sections appear in the file), using exactly this format:

```
[<section_name>] host=<host_value> port=<port_value>
```

Each section gets its own line. No blank lines between entries, no trailing spaces, no header or footer text — just the entries, one per line.

For example, if the INI file had a section `[staging]` with `host = staging.example.com` and `port = 8080`, the corresponding line in the summary would be:

```
[staging] host=staging.example.com port=8080
```

After creating the summary file, also append a final line to `/home/user/project/deploy.ini` itself (at the very end of the file):

```
; summary generated
```

That semicolon-prefixed line is an INI comment and should be the last line of the file.
