As a database administrator, you want to optimize SQL query performance by identifying which queries are causing slowdowns. You have a database query log file located at <code>/home/user/db/query.log</code>. 

The log file contains entries in the following format:
<pre>
[YYYY-MM-DD HH:MM:SS] user:USERNAME db:DBNAME duration:XXXms query:SQL_STATEMENT
</pre>
For example:
<pre>
[2024-06-20 13:27:14] user:alice db:invoices duration:205ms query:SELECT * FROM payments WHERE amount &gt; 1000;
</pre>

You need to extract and list all lines where the query duration is greater than 200 milliseconds. Use a regular expression to filter these entries.

Once filtered, write only the matching log lines to a new file at <code>/home/user/db/slow_queries.log</code>. The output in <code>slow_queries.log</code> must include the *entire original log lines*, in the same order as they appeared in the source file. Ensure the output log contains no extra blank lines before, between, or after the result entries.

This task will be considered complete when the <code>/home/user/db/slow_queries.log</code> file contains every query with a duration strictly greater than 200ms, based on the format shown above.
