You are a monitoring specialist tasked with setting up an alert system for a local application called "optim-solver". This application writes its logs to the file <code>/home/user/logs/optim-solver.log</code>. Your goal is to monitor this file for warning and error messages. 

Please complete the following steps:
1. Search for lines that contain the words "WARNING" or "ERROR" (case-sensitive) in <code>/home/user/logs/optim-solver.log</code>.
2. Write <b>only</b> those lines, in their original order, to a new file called <code>/home/user/alerts/optim-solver-alerts.log</code>. 
3. The alert file (<code>/home/user/alerts/optim-solver-alerts.log</code>) should only contain the relevant lines and nothing else (no headers, no extra whitespace or blank lines).
4. Confirm you have created the file by displaying the contents of <code>/home/user/alerts/optim-solver-alerts.log</code> in the terminal.

The automated test will check that the <code>optim-solver-alerts.log</code> file contains exactly the lines from the original log file that include "WARNING" or "ERROR", in the same order as they appear, and that you display those lines as your final output.
