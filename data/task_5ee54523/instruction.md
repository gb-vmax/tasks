You are a data engineer who needs to run a legacy ETL Python script to process a set of CSV sales records and verify the output. 

Here’s what you need to do:  
1. In the directory /home/user/etl_legacy/, there is a script called run_etl.py and an input file called sales_raw.csv.  
2. Run the run_etl.py script to process the sales_raw.csv file. The script reads sales_raw.csv and produces a file named sales_processed.csv in the same directory (/home/user/etl_legacy/).  
3. After the script finishes, display the full contents of the generated sales_processed.csv file on the terminal. This output must include all header rows and all records, formatted exactly as a comma-separated values (CSV) file.  
4. Additionally, create a log file named etl_run.log in /home/user/etl_legacy/ that contains the following two lines:
   - The first line should be the exact timestamp when you executed the ETL script, in ISO 8601 format (e.g., 2024-07-01T09:32:00)
   - The second line should be the message: ETL run completed successfully.

The completion of the task will be verified by checking:
- The existence and CSV format of /home/user/etl_legacy/sales_processed.csv, matching the expected output.
- The contents of /home/user/etl_legacy/etl_run.log containing the correct timestamp and message.
