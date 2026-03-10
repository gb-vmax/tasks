I manage a binary artifact repository and I need your help reformatting an artifact inventory report. I have a pipe-delimited file at `/home/user/artifacts/inventory.psv` that contains metadata about binaries stored in our repository. The file has 6 columns in this order:

```
artifact_name|version|arch|checksum_sha256|size_bytes|upload_date
```

I need to generate a trimmed report file at `/home/user/artifacts/report.psv` that:

1. Contains only the columns: `artifact_name`, `checksum_sha256`, `size_bytes`, and `upload_date` — in that exact order, dropping `version` and `arch`.
2. Prepends a new first column called `repo_id` to every row (including the header). The `repo_id` values come from a separate file at `/home/user/artifacts/repo_ids.txt`, which has one `repo_id` per line (the first line corresponds to the header row, the second line to the first data row, and so on).
3. The final output should be pipe-delimited, with the columns in this order: `repo_id|artifact_name|checksum_sha256|size_bytes|upload_date`

The output file `/home/user/artifacts/report.psv` must contain exactly the same number of lines as the input `inventory.psv` (including the header), with no trailing whitespace or blank lines.

Use standard Linux tools (`cut`, `paste`, etc.) to accomplish this. Please produce the file `/home/user/artifacts/report.psv` with the correct contents.
