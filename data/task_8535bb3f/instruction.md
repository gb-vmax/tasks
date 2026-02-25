You are a monitoring specialist tasked with setting up alerts for a database migration process. A sample sqlite3 database file named <b>/home/user/source_data.db</b> contains a table <b>employee</b> with the schema: <b>(id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)</b>. Your goal is to migrate all data from this source database to a new sqlite3 database called <b>/home/user/destination_data.db</b>, preserving schema and data.

After migration, create a validation report at <b>/home/user/migration_report.txt</b> with the following format:
<ul>
  <li>The first line: <b>TOTAL ROWS MATCH: YES|NO</b> (YES if both databases have the same row count in the 'employee' table, NO otherwise).</li>
  <li>The second line: <b>DATA INTEGRITY: PASSED|FAILED</b> (PASSED if every row in <b>destination_data.db.employee</b> matches <b>source_data.db.employee</b> exactly for all columns and row order, FAILED otherwise).</li>
  <li>Each subsequent line must be: <b>source_row={...} destination_row={...}</b> (showing the actual row from source and destination for each id in ascending order, formatted as Python dicts).</li>
</ul>
The validation report must strictly follow the described format, so it can be automatically checked. You may use any installed Linux tools and scripting languages. The alert setup is complete when <b>migration_report.txt</b> exists and its contents match the described format.
