You are a capacity planner analyzing basic system resource usage on a Linux workstation. Please generate a current snapshot that includes total memory, used memory, free memory, total number of CPUs, and the system load average for the last 1, 5, and 15 minutes. 

Save this information in the following plain text format (include the labels exactly as below, all values on a single line for each key):

Memory_Total_MB: [total memory in MB]
Memory_Used_MB: [used memory in MB]
Memory_Free_MB: [free memory in MB]
CPU_Count: [number of logical CPUs]
Load_Average_1min: [floating point number]
Load_Average_5min: [floating point number]
Load_Average_15min: [floating point number]

Place this output in a file named /home/user/resource_snapshot.log. 

Example output (your values will likely differ):

Memory_Total_MB: 7984
Memory_Used_MB: 2496
Memory_Free_MB: 5123
CPU_Count: 4
Load_Average_1min: 0.18
Load_Average_5min: 0.22
Load_Average_15min: 0.20

Do not include any extra text, headers, or formatting. The test will look for the specified key-value output in /home/user/resource_snapshot.log.
