You are a database administrator troubleshooting slow queries in your PostgreSQL database. There is a log file located at /home/user/db/postgresql.log. Each log entry is a single line in the following format:

[YYYY-MM-DD HH:MM:SS] user=<username> db=<dbname> duration=<number>ms statement: <SQL statement>;

Your task is to use regex-based filtering to extract all log entries where the duration is greater than or equal to 300ms. Do this by filtering only those lines where the duration field (duration=<number>ms) shows a value of 300 or above.

Write these filtered log lines (preserving their original format) to a new file named /home/user/db/slow_queries.log.

The output file, /home/user/db/slow_queries.log, must contain only those lines from the original log whose duration field is exactly 300ms or more. Entries with duration below 300ms must not appear. Keep the order of the original log. Do not add any extra characters or change the formatting.

To verify your solution, create a log file named /home/user/db/filter_log.txt. This file should record a single line of the form:

Filtered X slow queries into slow_queries.log

where X is the number of slow queries (i.e., lines with duration >= 300ms) that you extracted. Write only this line to the filter_log.txt file, with no additional text.
