You are assisting a script developer who is creating utilities to migrate data between two SQLite databases and validate the success of the migration. 

You will be given two SQLite database files in the directory /home/user/db-migration/: 
- source.db
- target.db

Both database files contain a table called "customers" with the following columns: id (INTEGER PRIMARY KEY), name (TEXT), and email (TEXT). The source.db contains 3 records; target.db is initially empty.

Your task is to:
1. Export all rows from the "customers" table in /home/user/db-migration/source.db into a CSV file called /home/user/db-migration/customers_export.csv. The CSV should have the header line: "id,name,email" and then one row per record, with values separated by commas. No extra whitespace or quotes should appear in the file.
2. Import all records from /home/user/db-migration/customers_export.csv into the "customers" table in /home/user/db-migration/target.db.
3. Validate that the data has been migrated correctly by querying the "customers" table in /home/user/db-migration/target.db, and write a validation log file at /home/user/db-migration/validation.log with the following exact format:
     - The first line should be: "Migrated X records to target.db", where X is the number of records (e.g. "Migrated 3 records to target.db")
     - The second line should be: "First customer: id=Y, name=Z, email=W" where Y, Z, W are the values of the first customer sorted by id (e.g. "First customer: id=1, name=Alice Smith, email=alice.smith@example.com")
     - There should be only two lines in the log file, no extra whitespace.

You should use standard command line tools (such as sqlite3) and scripts as needed. Do not generate any intermediate files not mentioned above, and do not modify any other files or directories on the system.
