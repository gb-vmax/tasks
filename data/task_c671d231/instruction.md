You are a machine learning engineer who needs to prepare your system for efficient model training. Before starting your data preparation, you want to monitor the current system resources to ensure your workstation is not overloaded. 

Please generate a resource snapshot log named <code>/home/user/ml_resource_snapshot.log</code> containing the following, in the exact order:

1. **CPU Usage:** Record the current CPU usage as a percentage averaged over all cores. Display this as a single line in the format: 
<pre>CPU Usage: X.Y%</pre>
where <code>X.Y</code> is the usage percentage (retain one decimal point).

2. **Available RAM:** Show the available RAM in megabytes (MB) in the format:
<pre>Available RAM: NNNN MB</pre>
where <code>NNNN</code> is the integer value of available RAM rounded down to the nearest whole number.

3. **Free Disk Space in /home:** Display the available disk space in the <code>/home</code> directory in gigabytes (GB), in the format:
<pre>Free Disk Space in /home: M.GB GB</pre>
where <code>M.GB</code> is the value rounded to two decimal points.

Append all three lines in this exact order (no extra text, headers, or blank lines) to the log file <code>/home/user/ml_resource_snapshot.log</code>. If the log file already exists, overwrite it. This file will be used to verify current system status before data preparation.
