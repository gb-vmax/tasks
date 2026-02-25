You are a system administrator managing monitoring agents on a group of servers. You have been provided with an INI-format configuration file located at <code>/home/user/server_config/monitoring.ini</code>. This file contains sections for multiple servers, each with several configuration keys.

Your task is to parse <code>/home/user/server_config/monitoring.ini</code> and generate a summary report. The report should extract the following fields from each server section: <b>hostname</b>, <b>ip</b>, <b>enabled</b>, and <b>interval</b>. The output summary must only include servers where <b>enabled = true</b> (case-insensitive) and must present the data in a specific CSV format.

Instructions:
<ul>
<li>Read the file <code>/home/user/server_config/monitoring.ini</code> and parse all sections that represent servers. Section names for servers start with <code>server_</code> (e.g., <code>[server_web01]</code>). Ignore any other sections.</li>
<li>From each server section, extract the fields: <code>hostname</code>, <code>ip</code>, <code>enabled</code>, and <code>interval</code>. If any of these are missing for a server, skip that server in the summary report.</li>
<li>Only include servers where the <code>enabled</code> field is set to <b>"true"</b> (case-insensitive).</li>
<li>Write a CSV report to <code>/home/user/server_config/active_servers.csv</code> with the following format:</li>
</ul>

<pre>
hostname,ip,interval
web01,192.168.10.10,60
db01,192.168.10.20,120
...
</pre>

<ul>
<li>The first row of the file must be the headers: <code>hostname,ip,interval</code></li>
<li>Each subsequent row represents an active server, with values as found in the INI file.</li>
<li>List servers in the order in which their sections appear in <code>monitoring.ini</code></li>
</ul>
When completed, verify that your summary report has been written correctly to <code>/home/user/server_config/active_servers.csv</code> following the specified format and contents.
