I have a SQLite database file located at /home/user/projects/tasks.db. I need a simple report of all entries in the "files" table, which has the following columns: id (integer), filename (text), project (text), and date_added (text, in YYYY-MM-DD format). 

Please query all data from the "files" table and output the results in plain-text, comma-separated CSV format (with the columns in order: id, filename, project, date_added). The first row must be the column headers. There must be no extra columns, trailing spaces, or blank lines. Print the CSV directly to the console.

Example of the required format:
id,filename,project,date_added
1,main.py,alpha,2024-05-01
2,README.md,alpha,2024-05-02

Query the database and display the current contents of the "files" table in this precise CSV format.
