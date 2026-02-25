You are a platform engineer tasked with updating CI/CD pipeline audit data formats and preparing input for a new dashboard system. Here’s what you need to do:

1. You receive a CSV file at <code>/home/user/audit_runs.csv</code> with columns: <code>run_id,pipeline,developer,start_time,status,duration_seconds</code>. Example rows:
<pre>
run_id,pipeline,developer,start_time,status,duration_seconds
1001,deploy-api,alice,2024-05-20T08:15:00Z,success,130
1002,deploy-web,bob,2024-05-20T08:17:23Z,fail,95
1003,deploy-api,charlie,2024-05-20T09:01:11Z,success,110
</pre>

2. Transform this file into a JSON Lines file at <code>/home/user/audit_runs.jsonl</code> where each line is a valid JSON object with fields: <code>run_id</code> (int), <code>pipeline</code> (str), <code>developer</code> (str), <code>start_time</code> (str, unchanged), <code>status</code> (str), <code>duration_seconds</code> (int). Maintain original order.

3. Next, generate a summary CSV at <code>/home/user/audit_summary.csv</code> with columns: <code>pipeline,total_runs,success_count,fail_count,average_duration</code>, ordered by pipeline name ascending. The summary must report, for each unique pipeline value:
   * <code>total_runs</code>: number of runs for this pipeline,
   * <code>success_count</code>: number of runs with <code>status</code>=success,
   * <code>fail_count</code>: number of runs with <code>status</code>=fail,
   * <code>average_duration</code>: integer average (rounded down) of <code>duration_seconds</code> for all runs on that pipeline.

4. Save a log file at <code>/home/user/audit_task.log</code> containing, line by line:
   * "JSONL generated: /home/user/audit_runs.jsonl"
   * "Summary CSV generated: /home/user/audit_summary.csv"
Each line must end with a newline.

Be sure that all generated files have precise headers and formatting, so they can be validated automatically.
