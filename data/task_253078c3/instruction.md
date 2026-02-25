You are acting as a Kubernetes operator analyzing onboarding logs for a manifest deployment process. In the directory <code>/home/user/kube-manifests/logs</code>, there is a log file named <code>deploy_onboarding.log</code>. This log captures the output from an automated deployment tool and contains mixed-level log entries (INFO, WARNING, ERROR).

Your task is to extract and count only the <b>ERROR</b> entries from <code>deploy_onboarding.log</code> and write the results to a new file called <code>/home/user/kube-manifests/reports/error_summary.log</code>. 

The output format for <code>error_summary.log</code> must list each unique ERROR message (without timestamp or log level prefix) with the number of its occurrences, sorted alphabetically by error message. The format for each line should be:

<pre>
[Error message text]: [count]
</pre>

For example, if the log contains:
<pre>
2024-06-14 10:00:00 ERROR deployment failed: missing image registry.example.com/app:latest
2024-06-14 10:01:00 ERROR unable to connect to API server
2024-06-14 10:02:00 ERROR deployment failed: missing image registry.example.com/app:latest
</pre>
The output should be:
<pre>
deployment failed: missing image registry.example.com/app:latest: 2
unable to connect to API server: 1
</pre>

Make sure:
<ul>
  <li>You only consider <code>ERROR</code> log entries (matching the string "ERROR" exactly).</li>
  <li>You remove timestamps and the word <code>ERROR</code> from each log entry, keeping only the error message text after the log level.</li>
  <li>You count and group identical error messages together.</li>
  <li>Your result file <code>error_summary.log</code> is sorted alphabetically by the error message text, one line per unique message.</li>
</ul>
