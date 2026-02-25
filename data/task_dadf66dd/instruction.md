As a data scientist, you are preparing a CSV file for further optimization analysis. Please remove all rows from the file /home/user/data/dirty_data.csv where the column 'value' contains missing (empty) entries or entries that are not valid floating-point numbers. Save the cleaned dataset as /home/user/data/clean_data.csv.

After cleaning, generate a log file at /home/user/data/cleaning_log.txt that meets the following requirements:
- The first line should read: "Removed X rows due to invalid or missing values", where X is the actual count of rows that were removed.
- The second line should read: "Remaining rows: Y", where Y is the count of rows in the cleaned output (excluding the header).
- The third line should be a single word describing the status: "Success".

Ensure the output CSV (/home/user/data/clean_data.csv) retains the exact same header row as the input.
