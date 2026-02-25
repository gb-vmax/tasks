You are an observability engineer working on improving dashboard performance for your team. In your home directory, you will find a folder located at /home/user/observability/dashboard_config/. This directory contains several YAML files and a log file named audit.log. Your task is to:

1. Identify the file named dashboard_metrics.yaml in /home/user/observability/dashboard_config/ and increase the refresh interval of the dashboard from "30s" to "60s". The parameter is located under a key called "refresh_interval" in the YAML structure.
2. Add a comment line "# Increased refresh interval from 30s to 60s on request" directly above the "refresh_interval" entry to document the change.
3. Append an entry to the audit.log file (also in /home/user/observability/dashboard_config/) to record your action. The format for the new audit log entry should be:
   
   ```
   [YYYY-MM-DD HH:MM:SS] user: Refreshed dashboard_metrics.yaml interval to 60s
   ```
   Replace [YYYY-MM-DD HH:MM:SS] with the current date and time in UTC in the ISO 8601 format (e.g., 2024-06-24 15:42:17).
   
After completing your work, the automated system will verify:
- That dashboard_metrics.yaml exists and contains the updated refresh interval and appropriate comment.
- That the audit.log file contains an entry appended at the end, in the specified format, reflecting your change.
