I'm a security engineer rotating credentials across three systems. I have exported the current credentials from each system into separate files, but unfortunately each system's export has columns in a different order, and I need to consolidate everything into a single normalized rotation report.

Here's what I need you to do. All input files are in `/home/user/credentials/` and the final output goes to `/home/user/credentials/rotation_report.tsv`.

---

**Input files and their column layouts:**

**`/home/user/credentials/db_creds.tsv`** — tab-separated, columns are:
`password | username | host | port | service`

**`/home/user/credentials/api_creds.tsv`** — tab-separated, columns are:
`service | host | username | api_key | expiry`

**`/home/user/credentials/ssh_creds.tsv`** — tab-separated, columns are:
`host | username | key_fingerprint | port | service`

---

**What I need extracted from each file:**

For the final report I need exactly these five columns in this exact order:
`service | host | username | secret | port`

The mapping for each file is:
- **db_creds.tsv**: `service`→col5, `host`→col3, `username`→col2, `secret`=password(col1), `port`→col4
- **api_creds.tsv**: `service`→col1, `host`→col2, `username`→col3, `secret`=api_key(col4), `port` is not present — use the literal string `N/A` for every row
- **ssh_creds.tsv**: `service`→col5, `host`→col1, `username`→col2, `secret`=key_fingerprint(col3), `port`→col4

**Important for api_creds.tsv**: since there is no port column, you need to append `N/A` as the fifth column for every data row. The `expiry` column (col5) should be discarded entirely.

---

**Processing steps:**

1. For each of the three input files, extract and reorder the columns into the normalized order (`service`, `host`, `username`, `secret`, `port`) using `cut` and `paste`. Each file's data rows should be transformed independently (you can work on them in parallel or in sequence, but the final merge must happen after all three are processed). Skip/exclude the header row from each input file — the output should contain data rows only.

2. Combine all three transformed outputs into a single file `/home/user/credentials/rotation_report.tsv` with:
   - A single header line as the **first line**: `service	host	username	secret	port` (tab-separated)
   - Then all rows from db_creds.tsv (in original order), followed by all rows from api_creds.tsv (in original order), followed by all rows from ssh_creds.tsv (in original order)

3. After creating the rotation_report.tsv, produce a summary file at `/home/user/credentials/rotation_summary.txt` with the following exact format (line by line, no extra blank lines):

```
Total credentials: <N>
DB credentials: <N>
API credentials: <N>
SSH credentials: <N>
Services: <comma-space-separated sorted unique list of service names>
```

Where the counts refer to data rows only (not the header), and Services lists each unique value from the `service` column of the final report, sorted alphabetically, joined with `, `.

---

The automated tests will check the exact contents of both output files, so please make sure column order, delimiters (tabs), and the summary format match exactly.
