I'm a backup administrator and I need your help parsing our nightly backup log file to create an archive summary report. The log is at `/home/user/backups/backup_nightly.log` and it contains mixed output from multiple backup jobs.

I need you to do the following:

**Step 1:** Extract only the lines that indicate a completed backup job. These lines match the pattern: they start with a timestamp in the format `[YYYY-MM-DD HH:MM:SS]`, followed by a space, the word `COMPLETED`, a space, and then the job name (a single word with no spaces). An example line looks like:

```
[2024-11-03 02:14:37] COMPLETED db_primary_backup
[2024-11-03 02:31:05] COMPLETED media_archive
```

There are also lines with `STARTED`, `FAILED`, `WARNING`, and plain info lines in the log — ignore all of those.

**Step 2:** From the extracted COMPLETED lines, reformat each one so the output has exactly this format (one job per line):

```
Job: <job_name> | Completed at: <YYYY-MM-DD> <HH:MM:SS>
```

For example, the line `[2024-11-03 02:14:37] COMPLETED db_primary_backup` should become:

```
Job: db_primary_backup | Completed at: 2024-11-03 02:14:37
```

**Step 3:** Write all the reformatted lines to `/home/user/backups/archive_summary.txt`. The lines should appear in the same order as they appeared in the original log file. There should be no blank lines, no header, no footer — just the reformatted job lines, one per line.

Can you produce this `archive_summary.txt` file for me?
