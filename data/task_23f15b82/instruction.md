I am a capacity planner and I need to quickly understand the current CPU and memory usage on the system to include in my report. Please generate a report that provides the following information in exactly this format:

CPU Usage: X%
Memory Usage: Y% (Z MiB / W MiB)

Where:
- X is the current overall CPU usage as an integer percentage (rounded to the nearest whole number), not a per-core breakdown.
- Y is the percentage of memory used, reported as an integer percentage (rounded to the nearest whole number).
- Z is the amount of memory currently used, in mebibytes (rounded to the nearest whole number).
- W is the total available memory, in mebibytes (rounded to the nearest whole number).

Write just these three lines (with values) to a file named /home/user/capacity_report.txt. Make sure the format exactly matches the example, with no extra spacing or blank lines. For example:

CPU Usage: 17%
Memory Usage: 32% (822 MiB / 2562 MiB)

I will verify that the data is current at the time the report was created. Ensure that you have sufficient permissions to write to the output file.
