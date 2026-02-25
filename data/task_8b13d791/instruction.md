You are a data scientist and need to clean a sample dataset log file using regex-based filtering. In your home directory (/home/user), you will find a file named /home/user/sample_data.log. This log file contains multiple lines in the following format:

[YYYY-MM-DD HH:MM:SS] STATUS - message

For example:

[2023-03-11 09:10:05] INFO - Import task started
[2023-03-11 09:10:07] ERROR - File not found
[2023-03-11 09:12:02] WARNING - Deprecated API usage

Your task is to:
1. Use regex-based filtering tools available in the Linux terminal to extract only those lines where the STATUS is "ERROR" or "WARNING" (matching case-sensitive, exactly these words).
2. Save the filtered results into a new file called /home/user/filtered_errors_warnings.log.
3. Ensure that the output file only contains the matching lines, in the exact same format as the original (no extra spaces, no line numbers, no other editing).

The automated test will check that /home/user/filtered_errors_warnings.log contains only the lines from /home/user/sample_data.log with STATUS of "ERROR" or "WARNING", and that all formatting is preserved exactly as in the original lines.
