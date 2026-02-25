You are a localization engineer updating translation data. You will find a CSV file at <code>/home/user/translations.csv</code> which contains English phrases and their French translations, but a few translations are missing. The file has the following columns: <code>key</code>, <code>en</code>, and <code>fr</code>.

Your task:

1. Update the file so that the French translation for the <code>greeting</code> key is changed from "Bonjour" to "Salut".
2. Fill in the missing French translation for the key <code>farewell</code> with "Au revoir".
3. Save the updated data as a new JSON file at <code>/home/user/translations_fr.json</code>, using the following format:
    <ul>
      <li>The top-level object should have English phrase keys and their corresponding French translation values (do not include the column names as keys).</li>
      <li>For example, if the CSV had a row: <code>welcome,Welcome,Bienvenue</code>, the JSON will have <code>"Welcome": "Bienvenue"</code>.</li>
    </ul>
4. Ensure the resulting JSON file is pretty-printed with an indentation of 2 spaces.

Example format of the JSON file (your actual values will differ, match the CSV content):

<pre>
{
  "Hello": "Salut",
  "Goodbye": "Au revoir"
}
</pre>

When finished, verify that the updated JSON file at <code>/home/user/translations_fr.json</code> matches these requirements exactly.
