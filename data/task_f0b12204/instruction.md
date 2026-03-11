Hey, I need your help with a quick data integrity check on our backup manifest file. I'm a backup engineer and I need to verify which backup entries are valid before we proceed with a restore operation.

We have a backup manifest at `/home/user/backups/manifest.json`. It's a JSON file with a top-level key `"backups"` that contains an array of backup entry objects. Each entry has these fields:

- `"id"`: a string identifier (e.g., `"bkp-001"`)
- `"filename"`: the backup filename (e.g., `"db_full_20240301.tar.gz"`)
- `"size_bytes"`: an integer representing the file size
- `"checksum"`: either a string (the SHA256 hash) or `null` if the checksum was never computed
- `"status"`: a string, either `"complete"` or `"partial"`

A backup entry is considered **valid** if ALL of the following are true:
1. `size_bytes` is greater than `0`
2. `checksum` is not `null`
3. `status` is `"complete"`

Please do the following:

**Step 1:** Use `jq` to filter the `backups` array and extract only the **valid** entries. From each valid entry, output only the `id` and `filename` fields. Write the result as a JSON array to `/home/user/backups/valid_backups.json`. The output should be a plain JSON array (not wrapped in any object), formatted with standard `jq` pretty-printing (2-space indentation). The entries should appear in the same order as they appear in the original manifest.

**Step 2:** Count how many valid entries there are and write a plain text summary to `/home/user/backups/integrity_report.txt`. The file should contain exactly one line in this format:

```
Valid backups: N/M
```

Where `N` is the number of valid backup entries and `M` is the total number of entries in the `backups` array. No trailing newline issues — just a single line ending with a newline character.

For example, if there are 3 valid backups out of 5 total, the file should contain exactly:
```
Valid backups: 3/5
```

Both output files should exist when you're done. Please use `jq` for the JSON processing parts.
