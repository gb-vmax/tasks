Hey, I'm managing a set of application configurations and I need your help extracting a summary from a JSON file into a CSV format that our reporting tool can ingest.

I have a configuration registry file at `/home/user/configs/registry.json`. It contains a JSON array of configuration objects. Each object has these fields:

- `service`: the name of the service (string)
- `env`: the deployment environment (string, one of: `production`, `staging`, `development`)
- `last_modified`: a date string in `YYYY-MM-DD` format
- `enabled`: a boolean indicating whether the config is active
- `version`: a version string like `"1.0.0"`

I need you to produce a CSV file at `/home/user/configs/summary.csv` that:

1. Contains only the entries where `enabled` is `true`.
2. Has exactly these columns in this order: `service,env,version,last_modified`
3. Includes a header row as the first line.
4. Is sorted alphabetically by `service` name (A to Z).
5. Does NOT include the `enabled` column in the output.

The CSV must use Unix line endings (no carriage returns), and there should be no trailing spaces or extra blank lines at the end of the file.

For example, if the registry had two enabled entries for services `zebra` and `alpha`, the output should list `alpha` first.

Can you parse the JSON file and write out the correctly filtered, sorted, and formatted CSV?
</think>
