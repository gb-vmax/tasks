You are a security engineer responsible for rotating user API keys. In the directory <b>/home/user/security/</b>, there is a CSV file named <b>api_credentials.csv</b> with the following two columns: <b>username</b> and <b>apikey</b> (no extra spaces, headers in lowercase). You need to automate the rotation of the API key for the user <b>alice</b>. 

Replace <b>alice</b>'s current <b>apikey</b> value with the new value <b>NEW_SECURE_API_KEY_8901</b>. Keep all other users and data unchanged, preserving the CSV layout, with the first line as the header and each following line as one user's credentials (all fields comma-separated, no extra spaces). Overwrite the original file, so that <b>/home/user/security/api_credentials.csv</b> reflects this change.

Finally, create a verification log file at <b>/home/user/security/rotation_log.txt</b> that contains exactly one line: <br>
<code>alice's API key rotated to NEW_SECURE_API_KEY_8901</code>

Do not change permissions or ownership of any files or directories.
