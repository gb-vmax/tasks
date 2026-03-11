I'm a backup engineer and I need your help verifying that a database migration completed successfully. We ran a migration last night that moved data from our original database to a new one, and I need to confirm the data integrity before we decommission the old system.

We have two SQLite databases:
- **Source database**: `/home/user/databases/source.db`
- **Migrated database**: `/home/user/databases/migrated.db`

Both databases have the same schema with a single table called `customers` with these columns:
- `id` (INTEGER)
- `name` (TEXT)
- `email` (TEXT)
- `balance` (REAL)
- `created_at` (TEXT)

Please perform the following integrity checks and write a verification report to `/home/user/databases/migration_report.txt`.

**Checks to perform:**

1. **Row count check**: Count the total number of rows in `customers` in both databases. Report whether they match.

2. **Balance sum check**: Compute the sum of the `balance` column (rounded to 2 decimal places) in both databases. Report whether they match.

3. **Email uniqueness check**: Count the number of distinct `email` values in each database. Report whether the counts match.

4. **Missing records check**: Find any `id` values present in the source database but missing from the migrated database. List them if any exist, or report none.

**The report file must follow this exact format** (including spacing, punctuation, and capitalization):

```
=== MIGRATION INTEGRITY REPORT ===

[CHECK 1] Row Count
  source: <N>
  migrated: <N>
  status: PASS

[CHECK 2] Balance Sum
  source: <X.XX>
  migrated: <X.XX>
  status: PASS

[CHECK 3] Email Uniqueness
  source distinct emails: <N>
  migrated distinct emails: <N>
  status: PASS

[CHECK 4] Missing Records
  missing IDs: none
  status: PASS

=== OVERALL: PASS ===
```

- For any check where the values differ, the `status:` line should say `FAIL` instead of `PASS`.
- For Check 4, if there are missing IDs, the line should read `  missing IDs: <id1>, <id2>, ...` (comma-space separated, in ascending numeric order).
- The `=== OVERALL: ===` line at the bottom should say `PASS` only if ALL four checks passed; otherwise it should say `FAIL`.
- Balance values must be formatted to exactly 2 decimal places (e.g., `1500.00`, not `1500.0` or `1500`).
