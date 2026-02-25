You are managing log files for a set of containerized microservices. In the directory /home/user/microservice_logs/, there are three log files: api.log, db.log, and cache.log. 

Your task is as follows:

1. For each log file, extract all lines containing the word "ERROR" (case-sensitive).
2. Combine these extracted "ERROR" entries from all three files, in the order: api.log, db.log, then cache.log.
3. Save the combined list into a new file named /home/user/microservice_logs/error_summary.log.
4. Each entry in error_summary.log should be prefixed with the original log file name in uppercase, followed by a colon and a space. For example, an error from api.log should appear as:
   ```
   API.LOG: [original error line]
   ```
   The order of the entries in error_summary.log must first list all from API.LOG, then DB.LOG, then CACHE.LOG, matching the order of the files processed.

Please perform this task and ensure that the error_summary.log file is created with entries formatted exactly as specified, ready for review.
