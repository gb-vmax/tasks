You are a support engineer collecting diagnostic information from a user's application configuration. In the directory <code>/home/user/appconfig</code>, there is an INI file named <code>settings.ini</code> with multiple sections, such as <code>[network]</code>, <code>[user]</code>, and <code>[database]</code>. 

Your task is as follows:
1. Parse <code>settings.ini</code> and extract all key-value pairs from the <code>[network]</code> section.
2. Create a diagnostics log file at <code>/home/user/appconfig/network_diagnostics.log</code>.
3. The log file must contain only the key-value pairs from the <code>[network]</code> section, each on its own line in the format: <code>key = value</code> (spaces around the equals sign), preserving the order they appear in the INI file. Do not include any section headers, comments, blank lines, or key-value pairs from other sections.
4. At the end of the log file, append a summary line in this exact format: <code>Total network parameters: N</code> where N is the number of key-value pairs you extracted.

Example <code>network_diagnostics.log</code>:
<pre>
hostname = app-host
port = 443
ssl_enabled = true
Total network parameters: 3
</pre>
