As a database reliability engineer, you are responsible for ensuring that regular backups of the database are both created and tracked. There is a SQLite3 database file located at <b>/home/user/data/customer_data.db</b>. Your task is to:

1. Create a backup of the SQLite3 database by copying <b>/home/user/data/customer_data.db</b> to <b>/home/user/backups/customer_data_backup.db</b>.
2. Verify the backup by running a SQL query on the backup file that lists all table names. Save the output to a log file named <b>/home/user/backup_logs/backup_verification.log</b>.
3. The verification log file must list the table names prefixed by <b>Table:</b> as shown below. The output format in <b>/home/user/backup_logs/backup_verification.log</b> must exactly match the following for automated validation:
<pre>
Table: customers
Table: orders
</pre>

The order of the tables must be as shown above. Directly run your SQL on the backup file and ensure the output is written in the specified format. 

Please ensure all actions use the specified file and directory paths.
