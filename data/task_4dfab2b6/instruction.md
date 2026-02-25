As a database reliability engineer, you want to securely manage PostgreSQL database backup credentials using environment variables and dotenv files. Please create a dotenv file at <b>/home/user/db_backup/.env</b> containing the following variables and values:

- <b>PGUSER</b> set to <b>db_backup_user</b>
- <b>PGPASSWORD</b> set to <b>S3cr3tP@ssw0rd2024</b>

Then, from a terminal session, load these variables into your session using the dotenv file, and verify that both environment variables are accessible and correctly set for the current shell. 

To finish, create a log file at <b>/home/user/db_backup/backup_env_check.log</b> with two lines in precisely the following format:
<pre>
PGUSER=db_backup_user
PGPASSWORD=S3cr3tP@ssw0rd2024
</pre>

Ensure that the file contains only those two lines, in that order, with no extra whitespace or newline at the end.
