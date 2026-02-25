You are a security engineer rotating credentials. In the directory <code>/home/user/creds</code>, you have a CSV file named <code>users.csv</code> containing user IDs, usernames, emails, and current API keys in the following format:

<pre>
user_id,username,email,api_key
1,alice,alice@example.com,oldkey-123
2,bob,bob@example.com,oldkey-456
3,charlie,charlie@example.com,oldkey-789
</pre>

You’ve generated a new file <code>new_keys.txt</code> with three new API keys, one per line (no header), such as:

<pre>
newkey-ab1
newkey-cd2
newkey-ef3
</pre>

Your task is to produce a new rotated user credentials file named <code>/home/user/creds/users_rotated.csv</code> that matches the exact following format requirements:

1. The file must have the **same header** as <code>users.csv</code>.
2. The **first three columns** (user_id,username,email) must come directly from the original <code>users.csv</code>.
3. The **fourth column** (<code>api_key</code>) must be the matching line from <code>new_keys.txt</code>, in order, so that each user gets their new key.
4. All fields must be comma-separated, with **no extra spaces** and no leading or trailing whitespace on any line.
5. There should be exactly one header and three user rows in the output file.

After completing the manipulation, create a verification log at <code>/home/user/creds/rotation_check.log</code> including the following (each item on a new line):

- "users_rotated.csv exists"
- "4 columns in header"
- "All api_keys are new"
- "Row count: 3"

This will be used by the automated test to ensure the task was performed correctly.
