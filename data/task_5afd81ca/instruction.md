You are a system administrator maintaining servers. A daily data pipeline on your server reads a CSV file, filters rows containing errors, and appends these to a log for later investigation. You suspect the script sometimes misses rows, so you want a simple, manual version you can run and verify.

In your home directory (/home/user), you will find an input file named <b>/home/user/server_data.csv</b>. Each line contains a timestamp, a status, and an error message, separated by commas, like this:

2024-06-01 14:22:38,OK,
2024-06-01 14:23:16,ERROR,Disk full
2024-06-01 14:25:02,ERROR,Network unreachable

Your task is:

1. Read <b>/home/user/server_data.csv</b>.
2. Extract all lines where the "status" field (the second column) is "ERROR".
3. Append these lines to a file called <b>/home/user/error_log.txt</b>. This file should remain in CSV format, and new error lines should be added to the end (do not remove any existing content in error_log.txt).
4. Output a count of how many error lines were appended in this operation on the console in exactly this format: 
<b>Appended N lines to /home/user/error_log.txt</b>
where N is the number of error lines added.

Ensure that the log file is correctly created if it does not exist, and that it keeps previous appended errors. If server_data.csv has no "ERROR" rows, do not change error_log.txt and output:
<b>No new error lines to append.</b>

A sample input and log file are present for testing. The automated test will verify the appended lines format and your console output.
