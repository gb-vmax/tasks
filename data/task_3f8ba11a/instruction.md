You are a platform engineer tasked with analyzing the build logs for a CI/CD pipeline to identify patterns in build failures.

1. Two hypothetical build log files are located in <b>/home/user/cicd_logs/</b> and named <b>build_log_2024-06-01.txt</b> and <b>build_log_2024-06-02.txt</b>.
2. Each log file contains multiple lines. Each line represents either a successful build or a failure. Failure lines always contain the phrase <b>BUILD FAILED</b> and an associated error message after a colon (e.g., "BUILD FAILED: DependencyError - missing package xyz").
3. Your task is to analyze <b>both</b> log files and summarize:
    - The number of total builds and failed builds (a build is represented by a line in the log).
    - The most common failure message (the text after "BUILD FAILED:").
    - A chronological list of unique failure messages encountered in both days.
4. Write a summary report to <b>/home/user/cicd_logs/build_failure_summary.txt</b> with the following <u>exact</u> format:

<pre>
Total builds: X
Failed builds: Y
Most common failure: [FAILURE_MESSAGE]

Unique failures:
DATE - FAILURE_MESSAGE
DATE - FAILURE_MESSAGE
...
</pre>

Where <b>DATE</b> matches the date in the filename ("2024-06-01" or "2024-06-02"), and each FAILURE_MESSAGE is the exact message text after "BUILD FAILED:" (preserving any leading/trailing whitespace).

<b>Important:</b>
<ul>
  <li>Do not include duplicate unique failures in the list, even if they happen on both days—list each unique message only once and on the date it first appeared.</li>
  <li>The order of "Unique failures" must be chronological by date, and within a date, by the line order in the log file.</li>
</ul>

When you have completed the task, print "<b>Log analysis complete. Summary written to /home/user/cicd_logs/build_failure_summary.txt</b>"
