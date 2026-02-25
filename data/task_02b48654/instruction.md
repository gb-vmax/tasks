You are migrating services as a cloud architect and need to analyze legacy system logs to identify failed deployment attempts before migration. In the directory <code>/home/user/migration/logs/</code> you will find a log file named <code>deployments.log</code>. 

Your task is to:
1. Filter <code>deployments.log</code> to extract all log entries (entire lines) containing the phrase <code>ERROR:</code> followed specifically by a non-empty service name (alphanumeric, dashes or underscores), whitespace, and then the phrase <code>deploy failed</code> (case-sensitive, exact match). Ignore <code>ERROR:</code> lines not matching this pattern. 
2. The filtered output should be saved to <code>/home/user/migration/logs/failed_services.log</code>.
3. The output format in <code>failed_services.log</code> must be one log line per matched entry, preserving the original order and exact whitespace of each line. No additional formatting, error messages, blank lines, or extra content should be present, only the matching log entries.

To verify, the automated test will compare <code>failed_services.log</code> to the exact expected filtered output based on the regex described above.
