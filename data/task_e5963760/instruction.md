You are maintaining a CI/CD pipeline and received a file containing build logs at <code>/home/user/builds/build_output.log</code>. This log file includes informational, warning, and error messages. Your job is to create a concise summary report that lists all unique error messages present in the log file.

To complete this task, please do the following:
1. Extract all lines from <code>/home/user/builds/build_output.log</code> that start with the text <code>ERROR:</code> (case-sensitive).
2. Remove any duplicate error lines so that each unique error message appears only once in the summary.
3. Save the unique error lines to a new file at <code>/home/user/builds/build_errors_summary.txt</code>.
4. The output file <code>build_errors_summary.txt</code> should:
    - Contain only the unique error lines, in the order they first appear in the input file.
    - Have each error message on its own line, with no extra blank lines at the beginning or end of the file.
    - Not include any lines that do not start exactly with <code>ERROR:</code>.

After completing your work, you can print the contents of <code>build_errors_summary.txt</code> to verify the output.
