You are a developer organizing project files on your Linux system. Please perform the following tasks to set up your environment and generate an output file:

1. Set your system's local time zone to "America/New_York" for your user session only. Confirm that the change has taken effect by outputting the current date and time in this timezone to a text file.
2. Set the locale for your user session to "de_DE.UTF-8" (German, Germany, UTF-8). Print the current locale configuration to verify the change.
3. Create a directory at <code>/home/user/project_env</code>. Within this directory, create two empty files: <code>app.py</code> and <code>README.md</code>.
4. In the file <code>/home/user/project_env/env_report.txt</code>, write a report in this exact format:
    <pre>
TIMEZONE: &lt;current time zone name&gt;
DATETIME: &lt;date/time in format YYYY-MM-DD HH:MM:SS&gt;
LOCALE: &lt;current locale string, line containing LANG=... from locale output&gt;
FILES:
- app.py FOUND
- README.md FOUND
    </pre>
The <code>DATETIME</code> entry should match the local time in the "America/New_York" timezone at the time the task is run, formatted as <code>YYYY-MM-DD HH:MM:SS</code> (for example, <code>2024-07-05 15:22:14</code>).
The <code>LOCALE</code> entry should be the line from the <code>locale</code> command output that starts with <code>LANG=</code>.
The <code>FILES</code> section must list "app.py" and "README.md" as "FOUND" if they exist in <code>/home/user/project_env/</code>, each on its own line with the required format.
Your report file is the only output that will be checked.
