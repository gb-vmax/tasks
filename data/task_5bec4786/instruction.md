You are a data engineer working on a small ETL (Extract, Transform, Load) pipeline. You are provided with a CSV file located at <b>/home/user/data/employees.csv</b> containing the following data:

<pre>
id,name,department,salary
1,Alice,Engineering,95000
2,Bob,Sales,70000
3,Charlie,Engineering,99000
4,David,HR,60000
</pre>

Your task is to use SQLite to perform the following steps:

1. Create a new SQLite database file at <b>/home/user/etl/employee_data.db</b>.
2. Import the data from <b>/home/user/data/employees.csv</b> into a table named <b>employees</b> in this database. The table should have columns corresponding to the headers in the CSV file, with types: id (INTEGER), name (TEXT), department (TEXT), salary (INTEGER).
3. Write and execute a SQL query that extracts all rows where the department is 'Engineering' and writes the output as a CSV file to <b>/home/user/etl/engineering_employees.csv</b>.
4. The output CSV file should be exactly formatted with the same headers as the input, containing only rows where employees are in the Engineering department (i.e., Alice and Charlie).

<b>The final output file (/home/user/etl/engineering_employees.csv) will be tested and must exactly match the following CSV format, including the header row:</b>

<pre>
id,name,department,salary
1,Alice,Engineering,95000
3,Charlie,Engineering,99000
</pre>
Ensure all directories exist before outputting files. Use only tools commonly available in base Linux and python environments (e.g., sqlite3, csv utilities, python3).
