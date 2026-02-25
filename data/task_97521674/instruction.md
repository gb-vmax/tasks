You are assisting as a localization engineer tasked with filtering translation update logs for further review. In the directory <code>/home/user/projects/translation_logs</code> you will find a log file named <code>update_20240612.log</code> containing entries in the following format:
<pre>
YYYY-MM-DD HH:MM:SS | locale:<i>LOCALE_CODE</i> | key:<i>TRANSLATION_KEY</i> | status:<i>STATUS</i> | details:<i>DETAILS</i>
</pre>
Where:
- <code>LOCALE_CODE</code> is a two-letter ISO language code (e.g., <code>fr</code>, <code>es</code>, <code>de</code>).
- <code>TRANSLATION_KEY</code> is a dotted identifier (e.g., <code>homepage.header.title</code>).
- <code>STATUS</code> is one of: <code>updated</code>, <code>added</code>, <code>failed</code>.
- <code>DETAILS</code> is free text, which may contain spaces or punctuation.

Please complete the following steps:

1. From the <code>/home/user/projects/translation_logs/update_20240612.log</code> file, extract only those lines where:
   - The <code>locale</code> is <code>fr</code> or <code>de</code>.
   - The <code>status</code> is either <code>failed</code> or <code>updated</code> (ignore <code>added</code>).
2. Save the filtered entries into a new file named <code>filtered_update_20240612.log</code> in the same directory (<code>/home/user/projects/translation_logs/filtered_update_20240612.log</code>).
3. Additionally, count and display (on the console) the total number of filtered entries, and append a one-line summary to the end of <code>filtered_update_20240612.log</code> in exactly this format:
<pre>
SUMMARY: <i>N</i> entries matching (locale: fr|de, status: failed|updated)
</pre>
where <code><i>N</i></code> is the number of matching entries you filtered.

Format Example:
If you filtered 7 matching lines, the summary should read:
<pre>
SUMMARY: 7 entries matching (locale: fr|de, status: failed|updated)
</pre>

**Note:**  
- Only use the provided directory and log file.  
- Do not change the original <code>update_20240612.log</code>.  
- Ensure your output exactly matches the specified summary format for automated verification.
