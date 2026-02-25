You are a data scientist preparing a CSV dataset for analysis. In your home directory (/home/user), you have a file named /home/user/raw_data.csv with the following exact content (including the header row):

id,name,age,department,salary,hire_date
1,Jane Doe,34,Engineering,92000,2018-06-21
2,John Smith,29,Marketing,67000,2019-12-01
3,Amy Adams,41,Engineering,105000,2016-03-17
4,Mark Lee,52,Human Resources,98000,2010-09-06
5,Leila Chan,37,Finance,88000,2015-11-23

Your goal is to create a cleaned dataset file located at /home/user/cleaned_data.csv with the following modifications:

1. Extract only the columns: name, department, salary (in that exact order).
2. Rearrange the extracted columns so that the order is: department, name, salary.
3. The cleaned_data.csv file must have the header row changed to: department,name,salary
4. There should be no additional whitespace, blank lines, or changes to data formats. All fields must remain exactly as in the original file.
5. Output file must be a valid CSV file (comma-delimited).
6. As verification, append (do not overwrite) a log entry to /home/user/processing.log after successful creation of cleaned_data.csv. The log entry should be a single line in this format (replace DATETIME with the current date and time in YYYY-MM-DD HH:MM:SS 24-hour format): 

[DATETIME] Cleaned data written to /home/user/cleaned_data.csv

The log file should preserve any pre-existing entries (if the log file does not exist, it should be created). The finished state of /home/user/cleaned_data.csv will be automatically checked against the specification above.
