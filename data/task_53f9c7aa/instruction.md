Hey, I'm an MLOps engineer and I need help analyzing an experiment artifact log. Our training pipeline writes a record to `/home/user/mlops/artifact_log.txt` every time it saves an artifact — one artifact type per line. I want to know how often each artifact type was saved so I can audit storage usage.

Please process `/home/user/mlops/artifact_log.txt` and produce a frequency report at `/home/user/mlops/artifact_counts.txt`.

The report should list each artifact type and how many times it appears in the log, sorted by count in **descending order** (highest count first). If two artifact types have the same count, sort them **alphabetically ascending** as a tiebreaker.

The output file must use this exact format — one artifact type per line, with the count and artifact type separated by a single space, count first:

```
<count> <artifact_type>
```

For example, a line might look like:
```
14 model_checkpoint
```

There should be no leading spaces, no blank lines, and no header line — just the raw data lines.

Write the result to `/home/user/mlops/artifact_counts.txt`.
