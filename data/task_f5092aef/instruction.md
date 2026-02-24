You are a localization engineer tasked with updating a set of translation strings for a software project. In the directory <b>/home/user/localization</b>, you will find a CSV file called <b>translations.csv</b>. Each row of the file represents a translation entry and contains three columns separated by commas: <b>key,en,fr</b> (header row included). The columns are as follows: 

- key: the identifier for the string
- en: the English translation
- fr: the French translation

Your tasks are as follows:

1. Extract only the <b>key</b> and <b>fr</b> columns (that is, the 1st and 3rd columns), maintaining their order, and save them in a new file named <b>/home/user/localization/fr_translations.csv</b>. This new CSV file should contain all the original rows, including the header, and must retain the order of lines from the input file.

2. Next, a set of updated French translations is provided in the file <b>/home/user/localization/fr_updates.csv</b>. This file contains two columns (key,fr) with updated French translations for some keys. The keys in <b>fr_updates.csv</b> exactly match some (but not all) keys from <b>translations.csv</b>.

3. Use <b>fr_updates.csv</b> to update <b>fr_translations.csv</b>: for any matching key, replace the French translation in <b>fr_translations.csv</b> with the value from <b>fr_updates.csv</b>. Make sure that any key present only in <b>fr_translations.csv</b> but not in <b>fr_updates.csv</b> remains unchanged. The row order and the header must remain unchanged.

4. Save the final, updated version as <b>/home/user/localization/fr_translations_updated.csv</b>.

<b>Output format requirements for /home/user/localization/fr_translations_updated.csv:</b>
- It must be a comma-separated values (CSV) file.
- The header row must be "key,fr".
- All original rows must be present in original order, with only the French translation values updated, where applicable.
- The file must contain no extra spaces, and columns must not be quoted.

As a final verification step, create a log file named <b>/home/user/localization/update_log.txt</b> listing each key whose French translation was updated, in the format: 
<pre>
key: &lt;key&gt; | old_fr: &lt;old value&gt; | new_fr: &lt;new value&gt;
</pre>
Each updated key should appear on its own line, matching the order they appear in <b>fr_translations.csv</b>. If no keys were updated, the log file should be empty.

Do not use any graphical interface; only use command line tools. 

Let me know when this is done and show me the paths and contents of the updated files as output.
