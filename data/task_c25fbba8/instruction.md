Our monitoring team has detected that multiple log files older than 7 days in the "/home/user/app/logs" directory might be linked to recent incidents. As an operations engineer, your task is to do the following:

1. Search recursively within "/home/user/app/logs" for all files ending with ".log" that were last modified more than 7 days ago.
2. For each log file found, count the number of lines that contain the word "ERROR" (case-sensitive).
3. Record your findings in a summary report at "/home/user/error_log_summary.txt". The output format in the summary report should have one line per log file, following this precise layout:
   
   ```
   <relative-path-from-/home/user/app/logs> ERROR_COUNT:<number-of-error-lines>
   ```

   For example:
   ```
   server1/server.log ERROR_COUNT:3
   api/debug.log ERROR_COUNT:0
   ```

- Only include ".log" files older than 7 days in the summary.
- Use relative paths from "/home/user/app/logs" (e.g., if the file is "/home/user/app/logs/a/b/c.log", the line should begin with "a/b/c.log").
- If a file contains no "ERROR", the count should be 0.
- Do not include any files that do not meet the above criteria.
- If no files are found matching the criteria, create an empty summary file at "/home/user/error_log_summary.txt".

Once you have completed the summary, check the contents of "/home/user/error_log_summary.txt" to verify your work.
