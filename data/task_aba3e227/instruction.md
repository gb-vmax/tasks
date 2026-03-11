I'm a cloud architect migrating services from one region to another, and I need your help processing a configuration file and generating a migration manifest.

There's a file at `/home/user/cloud/services.csv` that lists all our deployed services. Each line (after the header) has the format:

```
service_name,region,tier,monthly_cost_usd,replicas
```

I need you to do the following:

**Step 1: Filter services that need migration**

Only services currently in the `us-east-1` region that are in the `production` tier should be migrated. Extract those rows (not including the header) and write them to `/home/user/cloud/to_migrate.csv` — include the original header line as the first line of this file.

**Step 2: Generate the migration manifest**

Create a file at `/home/user/cloud/migration_manifest.txt` based on the filtered services. The manifest should:

- Start with a header line: `MIGRATION MANIFEST: us-east-1 -> eu-west-2`
- Follow with a separator line of exactly 40 dashes: `----------------------------------------`
- Then list each service that needs migration, one per line, in the exact format:
  ```
  [SERVICE] <service_name> | replicas=<replicas> | est_cost=$<monthly_cost_usd>
  ```
- After all services, add another separator line of exactly 40 dashes
- Then a line: `Total services: <count>`
- Then a line: `Total monthly cost: $<sum_of_monthly_costs>`

The services in the manifest should appear in the same order as they appear in `to_migrate.csv` (after the header). All cost values should be plain integers with no decimal places (they are already whole numbers in the source file). No trailing spaces on any line.

**Step 3: Set permissions**

Set the permissions on `/home/user/cloud/migration_manifest.txt` to `644`.

Please process the existing file at `/home/user/cloud/services.csv` and produce both output files as described.
