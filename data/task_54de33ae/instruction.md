As a network engineer troubleshooting connectivity issues, you are provided with a log file containing the results of multiple ping tests performed on various servers. The log file is located at <code>/home/user/ping_results.log</code>. Your task is to:

1. Count and display the total number of ping tests recorded in the log file.
2. Extract and display only the hostnames (or IP addresses) that had a result of "100% packet loss" (i.e., the server was unreachable).
3. Create a new filtered log file at <code>/home/user/unreachable_hosts.log</code>. This file must contain only those lines from the original log where the ping result was "100% packet loss", preserving the original line format.

**Log File Format (ping_results.log):**  
Each line in the file represents a single ping test and is formatted as:
<pre>
[YYYY-MM-DD HH:MM:SS] Host: &lt;hostname_or_IP&gt; Result: &lt;packet_loss_percent&gt; packet loss
</pre>
Example lines:
<pre>
[2024-06-06 08:31:22] Host: server1.example.com Result: 0% packet loss
[2024-06-06 08:31:23] Host: 192.168.0.42 Result: 100% packet loss
</pre>

**Output Required (for automated testing):**

- The total count (a single integer, no extra words or lines).
- A list of unreachable hostnames/IPs (one per line, no extra formatting or whitespace).
- The filtered log file <code>/home/user/unreachable_hosts.log</code> containing only the original "[...] Result: 100% packet loss" lines.
