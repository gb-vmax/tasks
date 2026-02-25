As a performance engineer, you are provided with an application profiling log located at <code>/home/user/profile.log</code>. Each line in the log contains information in the following format:

<pre>
PID: &lt;pid&gt;, CPU: &lt;cpu utilization percent&gt;%, MEM: &lt;memory usage MB&gt;MB, CMD: &lt;command name&gt;
</pre>

For example:
<pre>
PID: 4521, CPU: 23.1%, MEM: 125MB, CMD: myapp
PID: 4522, CPU: 88.6%, MEM: 300MB, CMD: data-collector
...</pre>

Your task is to identify all processes whose CPU utilization exceeds 50% and write their information into a new file at <code>/home/user/high_cpu_processes.txt</code>. The output file should only include these lines and should preserve the exact same format as the original log, without any additional whitespace, headers, or changes.

After generating this file, output the total number of high-CPU processes found (the number of lines in <code>/home/user/high_cpu_processes.txt</code>) to the terminal.

The correctness of your work will be verified by comparing the output file's contents and the printed count. Double-check that only the correct entries are included and the file's format exactly matches the described requirements.
