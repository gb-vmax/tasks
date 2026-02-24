You are a web developer tasked with migrating a small SQLite database from one file to another and validating the data migration. The source database file is located at /home/user/source.db and contains a single table named customers with three fields: id (integer), name (text), and email (text). 

Migrate all data from /home/user/source.db to a new database /home/user/destination.db, preserving the table structure and contents.

After the migration, perform a validation check to ensure the data in both databases is identical. 

To do this, generate a log file at /home/user/migration_validation.log. The log must include:

- The total number of rows in the "customers" table in both the source and destination databases.
- An entry stating whether the number of rows matches (Output must be: "Row count matches" or "Row count does not match").
- If the row counts match, also compare the content of every row between the two databases and provide an entry: "Row contents match" or "Row contents do not match".
- If the contents do not match, output a list of discrepancies, where each discrepancy is output on a new line in the format: "Discrepancy: [description]", where [description] is a brief description of the mismatch.

The format of the /home/user/migration_validation.log file must be:

Total rows in source: [number]  
Total rows in destination: [number]  
Row count matches (or) Row count does not match  
Row contents match (or) Row contents do not match  
Discrepancy: [description] (if any)

Make sure the log file is written exactly as specified for automated checking.
