You are managing a set of microservices running inside containers. There is a log file located at <code>/home/user/logs/microservice-app.log</code>, which contains entries in the following format:
<pre>
[TIMESTAMP] [SERVICE_NAME] [LEVEL] MESSAGE
</pre>
For example:
<pre>
2024-06-21T14:11:03Z auth INFO User logged in: id=74
2024-06-21T14:11:07Z payment ERROR Payment failed: code=500
2024-06-21T14:11:09Z auth WARN Token expired for user: id=74
</pre>
Your task is to produce a summary report file at <code>/home/user/logs/error_summary.txt</code> showing, for each microservice, the number of ERROR log entries. The output must list all services that had at least one ERROR entry, in the format:
<pre>
SERVICE_NAME ERROR_COUNT
</pre>
Each service should appear on a new line, with a single space separating the service name and the count. The list of services must be in alphabetical order.
For example, if only the "payment" service had two errors, the output file would be:
<pre>
payment 2
</pre>
If multiple services had ERROR entries, your report should look like:
<pre>
auth 3
payment 2
shipping 1
</pre>
Do not include informational output or summaries from other log levels. Make sure only services with at least one ERROR entry are listed.
