You are assisting a capacity planner in analyzing server resource usage data using SQLite via the command line. You will work with a database located at <code>/home/user/resource_usage.db</code>.

Perform the following steps:

1. Create a new table named <code>usage_stats</code> in the <code>resource_usage.db</code> database with the following columns:
    - <code>server_name</code> (TEXT)
    - <code>cpu_percent</code> (REAL)
    - <code>memory_mb</code> (INTEGER)
    - <code>timestamp</code> (TEXT)

2. Insert the following three records into <code>usage_stats</code>:
   <ul>
       <li><code>Alpha01</code>, <code>43.0</code>, <code>6084</code>, <code>2024-04-30T11:58:00Z</code></li>
       <li><code>Beta02</code>, <code>85.2</code>, <code>9560</code>, <code>2024-04-30T11:58:00Z</code></li>
       <li><code>Gamma03</code>, <code>22.7</code>, <code>4032</code>, <code>2024-04-30T11:58:00Z</code></li>
   </ul>

3. Query the database to return the following summary:
   - The <b>average CPU usage</b> (label the column as <code>avg_cpu_percent</code>).
   - The <b>maximum memory usage</b> (label the column as <code>max_memory_mb</code>).

   The output should have exactly two columns with these labels and a single row containing the results, separated by the pipe (<code>|</code>) character, as produced by SQLite's default CLI output for queries.

4. Save the query result in a text file at <code>/home/user/usage_summary.txt</code>.

The automated test will check that:
- The <code>usage_stats</code> table was created correctly with the specified columns and data types.
- The three records were inserted accurately.
- The file <code>/home/user/usage_summary.txt</code> exists and contains exactly one line (excluding any headers), with values for <code>avg_cpu_percent</code> and <code>max_memory_mb</code> separated by a single pipe (<code>|</code>).
- No additional lines or headers are present in <code>/home/user/usage_summary.txt</code>.
