Hey, I need your help analyzing a workflow execution log. I'm an automation specialist and I have a log file at `/home/user/automation/workflow_runs.log` that records the name of each workflow that was triggered (one workflow name per line). I need to figure out which workflows are running most frequently so I can prioritize optimization efforts.

Please process the log file and produce a frequency report at `/home/user/automation/workflow_frequency.txt`.

The report should list each unique workflow name along with how many times it appears in the log, sorted from most frequent to least frequent. If two workflows have the same count, sort them alphabetically by workflow name (ascending).

The output file must follow this exact format — one workflow per line, with the count and name separated by a single space and a colon, like this:

```
<count> <workflow_name>
```

For example, if `deploy_prod` ran 14 times and `backup_db` ran 3 times, the file should contain:

```
14 deploy_prod
3 backup_db
```

No leading spaces, no trailing spaces, no blank lines, and no header line — just the data rows in descending order by count.
