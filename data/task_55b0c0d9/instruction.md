You are a machine learning engineer preparing for a new training cycle. You currently have a small SQLite database at /home/user/ml_data/old_training_data.db, which contains a table named train_samples with three columns: id (INTEGER), sentence (TEXT), and label (INTEGER). You want to migrate all the data from this database into a new SQLite database at /home/user/ml_data/new_training_data.db.

After migrating the data, you need to validate the migration by generating a log file that compares the record count in the train_samples table in both databases, and confirms whether the migration was successful. The log file must be saved as /home/user/ml_data/migration_validation.log. 

The log file must be plain text, and must have the following format (replace the bracketed values accordingly):

Record count in old_training_data.db: [number]
Record count in new_training_data.db: [number]
Migration successful: [yes/no]

The line "Migration successful: yes" must only appear if the record counts in both databases are exactly equal, otherwise it should say "no". Please do not include any other text or extraneous output in the log file.
