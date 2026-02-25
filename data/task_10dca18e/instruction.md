You are a DevOps engineer tasked with debugging recent errors in an application. The application produces four daily rotating log files: <code>/home/user/logs/app_backend.log</code>, <code>/home/user/logs/app_frontend.log</code>, <code>/home/user/logs/app_worker.log</code>, and <code>/home/user/logs/app_scheduler.log</code>. Each file is in plain text, and may contain lines with the following log levels: <code>INFO</code>, <code>WARNING</code>, and <code>ERROR</code>.

Your assignments are as follows:

1. Write and save a shell script named <code>/home/user/scripts/extract_errors.sh</code> that will do the following tasks in parallel:
   - For each log file in <code>/home/user/logs/</code> whose name matches <code>app_*.log</code>:
       - Extract all lines containing the text <code>ERROR</code>.
       - Save the extracted lines to a new file with the same basename but the suffix <code>.errors</code> (e.g., <code>app_backend.errors</code>), in a new directory <code>/home/user/errors/</code>.
   - Ensure that extraction for each log file runs as a background process in the script, so that all are processed in parallel.
   - After spawning all background processes, the script should wait for all extraction jobs to finish before exiting.

2. Execute your script to perform the extraction.

3. In the directory <code>/home/user/errors/</code>, produce a summary file named <code>error_summary.log</code> with the following strict format:
   - Each line summarizes one log file’s errors and should be in this form (one line for each processed log file):
     <pre>
     &lt;LOG_FILENAME&gt;: &lt;ERROR_COUNT&gt; errors
     </pre>
      For example:
     <pre>
     app_backend.log: 3 errors
     app_frontend.log: 0 errors
     </pre>
   - The log files should be listed in alphabetical order by basename.

4. Confirm extraction and summary by displaying the contents of <code>error_summary.log</code> in your terminal output.

You have read and write permissions on the <code>/home/user/logs/</code>, <code>/home/user/scripts/</code>, and <code>/home/user/errors/</code> directories. You do not have root access. Be sure that your shell script uses background jobs for parallelism, not sequential processing. The script must be executable. The format of <code>error_summary.log</code> must exactly match the specification for automated testing.
