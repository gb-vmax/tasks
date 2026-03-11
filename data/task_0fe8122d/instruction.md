Hey, I'm a storage administrator and I'm running low on disk space in our data pipeline working directory. I need your help identifying which subdirectories under `/home/user/pipeline_data` are using the most space, so I can decide what to clean up.

Specifically, I need you to do the following:

1. Measure the disk usage of each **immediate subdirectory** inside `/home/user/pipeline_data` (not recursively — just the top-level subdirectories, but counting everything inside each one).

2. Write a report to `/home/user/disk_report.txt` that lists each subdirectory's usage in **human-readable format**, sorted from **largest to smallest**. The report must contain ONLY the `du` output lines — one line per subdirectory — in the format that `du -h` produces (e.g., `4.0K\t/home/user/pipeline_data/subdir`). No headers, no extra text, no blank lines.

The file at `/home/user/disk_report.txt` should be ready for me to review immediately after you run the commands. I'll be checking it automatically so the format needs to be exact.
