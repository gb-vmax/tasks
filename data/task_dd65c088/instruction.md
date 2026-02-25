You are assisting as a cloud architect migrating application services. A log file named <code>/home/user/migration/migration.log</code> contains entries of all services and their migration statuses. Each line is formatted as:
<pre>
[YYYY-MM-DD HH:MM:SS] service_name: STATUS
</pre>
Where <code>STATUS</code> can be either <code>SUCCESS</code> or <code>FAILURE</code>. For example:
<pre>
[2024-06-01 10:00:00] database: SUCCESS
[2024-06-01 10:05:10] cache: FAILURE
</pre>
Your task is to perform the following:
<ol>
    <li>Analyze the <code>migration.log</code> file and summarize how many services had a <code>SUCCESS</code> migration and how many had a <code>FAILURE</code>.<br>
    </li>
    <li>Create a new summary file at <code>/home/user/migration/migration_summary.txt</code>. This file must have exactly two lines, each in the following format:
    <pre>
Total SUCCESS: X
Total FAILURE: Y
    </pre>
Where <code>X</code> and <code>Y</code> are the respective counts found in <code>migration.log</code>.<br>
   </li>
</ol>
No other output or formatting is required. Ensure that the summary file contains only the two specified lines in the above format for automated tests.
