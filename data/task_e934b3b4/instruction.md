You are working as a data analyst in the /home/user/data_analysis directory, which contains several CSV files of varying sizes. Your goal is to perform a comprehensive disk usage analysis by completing the following steps:

1. For each CSV file in /home/user/data_analysis, determine its file size in bytes. 
2. Generate an output file named /home/user/data_analysis/csv_disk_usage_report.txt formatted as follows:
   - Each line should contain the file name (with the .csv extension), a comma, and the file size in bytes (no extra spaces).
   - The lines should be sorted in descending order by file size (largest first).
   - Example of the desired format for the report:
     ```
     large_dataset.csv,102408
     medium_dataset.csv,51423
     small_dataset.csv,14793
     ```
3. Simultaneously, create a summary statistics file named /home/user/data_analysis/csv_disk_usage_summary.txt, which must contain exactly three lines:
   - The first line: the total number of CSV files found in /home/user/data_analysis.
   - The second line: the total combined size (in bytes) of all these CSV files.
   - The third line: the average file size (rounded down to the nearest integer) in bytes.
   - Example of the desired format for the summary:
     ```
     3
     168624
     56208
     ```

Ensure your solution works for any arbitrary number and size of CSV files present in /home/user/data_analysis. Only .csv files located directly in /home/user/data_analysis should be included (do not search subdirectories). Do not include headers in either output file. Both output files must be created with the exact names and formats provided above so they can be automatically verified.
