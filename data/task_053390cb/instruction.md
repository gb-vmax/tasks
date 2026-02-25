You are assisting a capacity planner who needs to find the department with the highest average CPU usage from a CSV data file. In the file <b>/home/user/data/resource_usage.csv</b>, there are three columns: <i>department</i>, <i>server</i>, and <i>cpu_usage</i> (which holds a floating-point value representing CPU usage percentage for that server).

Your task is to analyze this CSV file and create a **single-line JSON file** at <b>/home/user/data/dept_with_highest_avg_cpu.json</b> containing two keys: <i>department</i> (string with department name) and <i>avg_cpu_usage</i> (rounded to two decimal places, as a number).

For example, if the "Marketing" department has the highest average CPU usage of 62.748, your output file should look exactly like this (the number rounded):

{"department": "Marketing", "avg_cpu_usage": 62.75}

Ensure there are no extra spaces, all JSON is lowercase for key names, and the file contains a single line. The result will be verified against this strict JSON serialization.
