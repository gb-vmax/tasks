You are a data analyst working in the /home/user/data directory, where there is a CSV file named sales_data.csv. Your task is to automate the process of extracting and summarizing data from this file using a shell script. Specifically, do the following:

1. Write a shell script named summarize_sales.sh, saved in /home/user/data/.
2. The script should:
   - Take /home/user/data/sales_data.csv as the input file.
   - Calculate the total sum of the values in the "Amount" column (the third column in the CSV, which contains only integer numbers and has a header).
   - Display the sum on the screen in the following format (replace 99999 with the actual total):  
     Total Sales Amount: 99999
   - Additionally, write the same output line to a new file called sales_summary.txt in the same directory (/home/user/data/sales_summary.txt).
3. Make sure the script can be executed without any input arguments and that file paths are used explicitly (not relative paths).
4. When finished, make sure that /home/user/data/sales_summary.txt exists and is formatted exactly as described above.

Summarizing: automate the summing of the "Amount" column in sales_data.csv and output a line ("Total Sales Amount: 99999") both to the terminal and to sales_summary.txt, using an executable script.
