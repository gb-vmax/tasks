Hey, I need your help collecting some diagnostic information from our application configs. We have two configuration files on this server and I need you to extract specific values from each one and write them into a standardized diagnostics file. This is for a support ticket we're filing with our vendor.

Here are the two config files:

**`/home/user/configs/service.yaml`** — a YAML file for our service configuration

**`/home/user/configs/app.toml`** — a TOML file for our application configuration

Please do the following:

1. From `/home/user/configs/service.yaml`, read these values:
   - `service.name`
   - `service.version`
   - `service.environment`
   - `database.host`
   - `database.port`

2. From `/home/user/configs/app.toml`, read these values:
   - `server.host`
   - `server.port`
   - `server.timeout`
   - `logging.level`
   - `logging.file`

3. Write a diagnostics file at `/home/user/diagnostics/report.txt` with **exactly** this format (substitute the actual values in place of the angle-bracket placeholders):

```
=== DIAGNOSTIC REPORT ===

[SERVICE]
name: <service.name>
version: <service.version>
environment: <service.environment>

[DATABASE]
host: <database.host>
port: <database.port>

[SERVER]
host: <server.host>
port: <server.port>
timeout: <server.timeout>

[LOGGING]
level: <logging.level>
file: <logging.file>
```

The file must end with a single newline after the last line (`file: ...`). There should be exactly one blank line between each bracketed section, and exactly one blank line between the `=== DIAGNOSTIC REPORT ===` header and the `[SERVICE]` section. No trailing spaces on any line.

Make sure the `/home/user/diagnostics/` directory exists before writing the file.
