You are a QA engineer preparing to validate application logs for an upcoming test environment setup. Within your home directory (/home/user), you have a large log file located at /home/user/logs/testapp.log. Your objective is to create a filtered overview of particular error and warning events observed during startup tests.

You need to do the following:

1. First, ensure that the /home/user/logs directory exists.
2. Create a new file at /home/user/logs/testapp.log containing at least the following 7 lines (order and additional non-critical lines are allowed):
    - "2024-04-11 10:12:01 INFO Starting application"
    - "2024-04-11 10:12:03 WARNING Deprecated configuration detected"
    - "2024-04-11 10:12:07 ERROR Failed to connect to database"
    - "2024-04-11 10:12:09 INFO Database retry attempt 1"
    - "2024-04-11 10:12:11 WARNING Low disk space"
    - "2024-04-11 10:12:13 ERROR Could not locate config file"
    - "2024-04-11 10:12:16 INFO Application shutdown complete"
3. Using regular expressions (regex), filter out and extract only the lines containing the words "WARNING" or "ERROR" (case-sensitive, matches only whole words), in the order they appear, from the original log file.
4. Save just those filtered lines (with exact original spacing and content as in the source) to a new file: /home/user/logs/filtered_report.txt
5. The final filtered report file (/home/user/logs/filtered_report.txt) must contain only the filtered lines (no extra whitespace or blank lines), in the exact same order as they appeared in testapp.log.
6. For verification, output the full absolute path name of the filtered report file as the final console output line.

The automated test will:
- Check that the filtered report contains exactly (and only) the correct lines, in order. Each line must match exactly, with no leading/trailing whitespace, extra blank lines, or omitted lines.
- Confirm that the final console output matches the path to the filtered report, i.e., "/home/user/logs/filtered_report.txt".

Carefully follow the requirements: only filter for lines with "WARNING" or "ERROR" using regex, and double-check the output format.
