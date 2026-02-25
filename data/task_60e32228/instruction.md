You are a localization engineer tasked with updating translation files for a web application. In the directory <code>/home/user/localization</code>, you will find three JSON translation files: <code>en.json</code> (English), <code>fr.json</code> (French), and <code>es.json</code> (Spanish).

Your task is as follows:

1. Extract all keys from <code>/home/user/localization/en.json</code> and verify that every key is also present in both <code>fr.json</code> and <code>es.json</code>. If any keys are missing from the French or Spanish files, add them to the appropriate file, using the English text as the value, but surround it with <code>[[MISSING_TRANSLATION]]</code> markers. For example, if the key <code>“logout”</code> is missing and its value in English is <code>“Logout”</code>, you should add <code>"logout": "[[MISSING_TRANSLATION]]Logout[[MISSING_TRANSLATION]]"</code> to the missing language file.

2. Remove any keys in <code>fr.json</code> or <code>es.json</code> that do not exist in <code>en.json</code>. Only keep the intersection of keys.

3. Reformat all three JSON files (<code>en.json</code>, <code>fr.json</code>, and <code>es.json</code>) so that keys are sorted alphabetically and each file has pretty-printed, 2-space indentation.

4. Save a log file named <code>/home/user/localization/update_report.log</code> with the following structure:
   - Section 1: “Missing keys added” — List all keys (one per line) that were added to each language file, with the language file name and key (e.g., <code>Added to fr.json: logout</code>).
   - Section 2: “Extra keys removed” — List all keys that were removed from each language file, with the language file name and key (e.g., <code>Removed from es.json: help</code>).
   - Section 3: “Final key count” — For each file, output the final number of keys, one line per file, using the format: <code>en.json: N keys</code>

At the end, all three JSON files must contain exactly the same set of keys (sorted alphabetically), and the log must reflect all additions and removals that occurred.
