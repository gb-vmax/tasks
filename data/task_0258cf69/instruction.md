You are acting as a database administrator who needs to optimize user transaction queries. The database has exported two files in your home directory:

1. A CSV file at <code>/home/user/user_transactions.csv</code> with the following columns: <code>user_id</code>, <code>username</code>, <code>transaction_id</code>, <code>amount</code>, <code>timestamp</code>, <code>status</code>. There are multiple users and each may have several transactions, each marked as <code>status</code> "completed" or "pending".

2. A JSON file at <code>/home/user/user_profiles.json</code> with an array of objects, each containing: <code>user_id</code>, <code>email</code>, <code>sign_up_date</code>, and <code>last_login</code>.

Your tasks are:

<ul>
  <li>1. Analyze the <code>/home/user/user_transactions.csv</code> file to identify all users (by <code>user_id</code> and <code>username</code>) who have more than <b>3 completed transactions</b>.</li>
  <li>2. For those identified users, extract their full profile from <code>/home/user/user_profiles.json</code> (matching by <code>user_id</code>) and generate a new JSON file at <code>/home/user/optimized_query_users.json</code>. This file must be an array of user profile objects, in the same format as the original, but <b>only</b> including users who match the "more than 3 completed transactions" criteria.</li>
  <li>3. Produce a summary report called <code>/home/user/optimization_report.csv</code> with the following columns: <code>user_id</code>, <code>username</code>, <code>completed_transaction_count</code>. Each row should represent an identified user for this optimization.</li>
</ul>

<b>Output Format Details:</b> 
<ul>
  <li>The <code>/home/user/optimized_query_users.json</code> file must be a valid JSON array, with each object containing the fields: <code>user_id</code>, <code>email</code>, <code>sign_up_date</code>, <code>last_login</code>, and <b>no additional fields</b>.</li>
  <li>The <code>/home/user/optimization_report.csv</code> must have the header exactly as specified (including lower-case and underscores) and then one row per user, in <code>user_id</code> numeric ascending order. Separate values with commas, no extra spaces.</li>
</ul>

To verify your solution, ensure that both new files are correctly formatted and only contain data for users with more than 3 completed transactions.
