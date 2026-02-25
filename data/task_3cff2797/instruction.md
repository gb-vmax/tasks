You are a data engineer preparing your environment for ETL pipelines. In your home directory (/home/user), there is an existing directory called /home/user/etl_data containing three CSV files: data1.csv, data2.csv, and data3.csv. Please create a compressed tar archive of the /home/user/etl_data directory using gzip compression (.tar.gz extension). Name the archive /home/user/etl_backup_2024_06_15.tar.gz.

After creating the archive, verify that the archive contains all three files (data1.csv, data2.csv, and data3.csv) at the root of the etl_data folder inside the archive (not nested further). Then, produce a plain text log file at /home/user/etl_backup_log.txt with the following structure:

- First line: "Backup completed on: <YYYY-MM-DD HH:MM:SS>" (use the current system date and time in 24-hour format)
- Second line: "Files in archive:"
- Subsequent lines: A list of the three CSV file names, one per line, in alphabetical order (data1.csv, data2.csv, data3.csv)

Do not include any extraneous output or file paths; the log file must precisely match the described format so that an automated test can verify the results.
