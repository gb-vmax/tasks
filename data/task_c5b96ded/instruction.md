As a configuration manager, you are reviewing a configuration file named <code>/home/user/system/config/settings.conf</code>. This file contains key-value pairs, one per line, in the format <code>key=value</code> (for example, <code>max_connections=10</code>). Some lines may contain comments that start with <code>#</code>, either at the beginning of the line or inline after an entry.

Your task is as follows:

1. Extract all key-value pairs where the <code>key</code> starts with the prefix <code>net_</code> (for example, <code>net_mode=auto</code>), ignoring any lines that are commented out (lines starting with <code>#</code>).
2. Remove any inline comments (starting with <code>#</code>) from these entries, so that only the pure <code>key=value</code> remains.
3. Save the processed results to a new file at <code>/home/user/system/logs/net_settings.log</code>, with each key-value pair on its own line, and no blank lines or comments in the output.

The output in <code>/home/user/system/logs/net_settings.log</code> should look like the following:

<pre>
net_mode=auto
net_timeout=30
</pre>

Use <code>awk</code> and <code>sed</code> as appropriate. The automated test will check that the output file exactly matches this format—one line per entry, no leading/trailing spaces, no blank lines, and no comments.
