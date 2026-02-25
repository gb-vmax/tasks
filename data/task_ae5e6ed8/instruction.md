You are a web developer who needs to analyze your application’s access logs for debugging and performance monitoring. In your home directory at <code>/home/user</code>, there is a directory called <code>logs</code> which contains a file named <code>access.log</code> with web server access logs. 

Your tasks are:

1. Parse the <code>/home/user/logs/access.log</code> file and extract the following:
    - The total number of requests.
    - The number of requests resulting in HTTP status code 404.
    - The unique IP addresses that accessed the server.
    - The hour (in HH format, 24h time) with the highest number of requests.
2. Write a summary report file at <code>/home/user/logs/analysis_report.txt</code> in the following exact format:

<pre>
Total Requests: &lt;total_requests&gt;
404 Errors: &lt;num_404&gt;
Unique IPs: &lt;comma-separated-list&gt;
Peak Hour: &lt;HH&gt; (&lt;num_requests&gt; requests)
</pre>

<code>&lt;comma-separated-list&gt;</code> must be the unique IP addresses sorted in ascending order, separated by commas (no spaces).
<code>&lt;HH&gt;</code> must be the hour in two-digit format (e.g. 14), and <code>&lt;num_requests&gt;</code> the count for that hour.

Your summary format and order must match exactly for automated checking.

Do not modify the original log file. Write only the summary report file with the required data.
