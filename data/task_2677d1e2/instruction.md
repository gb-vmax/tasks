I'm a cloud architect and I've been running a batch migration script that logs status updates as each service is moved to the new cloud environment. The log file is at `/home/user/migration/services.log`. Each line follows this format:

```
[TIMESTAMP] [STATUS] SERVICE_NAME :: MESSAGE
```

For example:
```
[2024-06-10 08:01:32] [SUCCESS] auth-service :: Migrated to us-east-2 successfully
[2024-06-10 08:03:11] [FAILED] billing-service :: Connection timeout during snapshot transfer
[2024-06-10 08:07:45] [SKIPPED] legacy-reporting :: Marked for decommission, skipping migration
```

I need a quick summary of which services failed so I can prioritize them for re-migration. Please do the following:

1. From `/home/user/migration/services.log`, extract only the lines where the status is `FAILED`.

2. From those failed lines, extract just the service name (the part between `[FAILED] ` and ` ::`).

3. Write those service names, one per line, **sorted alphabetically**, into a new file at `/home/user/migration/failed_services.txt`.

The output file `/home/user/migration/failed_services.txt` should contain **only the service names**, one per line, with no extra spaces, timestamps, brackets, or other text. For example, if `billing-service` and `api-gateway` both failed, the file should look exactly like:

```
api-gateway
billing-service
```

No trailing blank lines, no header, nothing else.
