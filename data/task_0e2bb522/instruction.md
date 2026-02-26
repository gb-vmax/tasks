You are triaging an incident as an operations engineer. You are given a web server access log located at <code>/home/user/logs/access.log</code>. Your task is to analyze the log for 404 errors and summarize your findings.

1. Search through the log file and extract all lines that represent HTTP 404 errors. A 404 error line is characterized by its status code being "404" (as the first three digits of the field immediately following the quoted request). The log is in standard Apache combined format (each log line contains: ip_address - - [date time zone] "method url protocol" status_code response_size referer user_agent).

2. Count the total number of 404 errors found in the log and write this number to a new file named <code>/home/user/triage/404_summary.txt</code>.

3. Also, identify the unique URLs that returned a 404 error, and list them, one per line, below the total count in the same file.

The required format for <code>/home/user/triage/404_summary.txt</code> is:

<pre>
404 count: X
Unique URLs:
<url_1>
<url_2>
...
</pre>

Be sure to create the <code>/home/user/triage/</code> directory if it does not exist. Only include the path of the URL (for example, "/notfound.html", not the full request string). Your output in <code>404_summary.txt</code> must exactly match the required format (including '404 count:' and 'Unique URLs:' as shown).
