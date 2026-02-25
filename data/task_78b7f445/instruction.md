You are a capacity planner responsible for analyzing resource usage on this Linux system. First, set your system timezone to "America/New_York" without requiring root privileges. Then, print out today's date and time using the `date` command, ensuring the output follows this precise format (in 24-hour time):

YYYY-MM-DD HH:MM:SS EDT

For example: 2024-06-01 14:30:15 EDT

Create a report file at /home/user/resource_usage_report.txt that contains exactly one line: the current date and time as printed above. The report file should not contain any additional information or formatting.

The automated test will verify the exact time zone abbreviation (EDT), the strict ordering and formatting of fields, and that only a single line is present in the report file. Do not include any explanation or extra output.
